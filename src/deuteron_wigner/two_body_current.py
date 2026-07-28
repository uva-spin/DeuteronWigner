"""Leading isoscalar chiral two-nucleon magnetic current.

Implements Kolling, Epelbaum, and Phillips, arXiv:1209.0837, Eq. (3), in the
two-nucleon spin space. Momenta and masses use GeV natural units. The deuteron
isospin matrix element ``tau_1 dot tau_2 = -3`` is used by default.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import simpson

from .light_front import _D_COUPLING, _spherical_harmonic_l2, _triplet_spin_amplitude
from .wavefunctions.models import RadialWaveFunction


NORFOLK_ISOSCALAR_LECS = {
    "nvia": (-0.00999, -0.06571),
    "nvib": (-0.02511, -0.02384),
    "nviia": (-0.01170, -0.04714),
    "nviib": (-0.04955, -0.07947),
}

# PRC 106, 044001 (2022), Table II, reference fit set A.  These are the
# post-Fierz dimensionless constants explicitly recommended by Alex Gnech.
NORFOLK_PRC106_SET_A_ISOSCALAR_LECS = {
    "nvia": (0.012, 0.023),
    "nvib": (0.025, 0.030),
    "nviia": (0.011, 0.019),
    "nviib": (0.017, 0.018),
}

# PRC 106, 044001 (2022), Table IV.  These are validation targets, not
# operator inputs.  The minimal-current row cannot be reconstructed by
# merely replacing the two fitted isoscalar constants in the PRC99 code.
NORFOLK_PRC106_SET_A_DEUTERON_MOMENTS = {
    "nvia": {
        "lo": 0.8499, "n2lo": -0.0062, "minimal": 0.0284,
        "d1": -0.0115, "d1_error": 0.0009,
        "d2": -0.0015, "d2_error": 0.0004, "total": 0.859,
    },
    "nvib": {
        "lo": 0.8486, "n2lo": -0.0062, "minimal": 0.0301,
        "d1": -0.021, "d1_error": 0.002,
        "d2": 0.008, "d2_error": 0.002, "total": 0.860,
    },
    "nviia": {
        "lo": 0.8500, "n2lo": -0.0065, "minimal": 0.0271,
        "d1": -0.0100, "d1_error": 0.0009,
        "d2": -0.0011, "d2_error": 0.0004, "total": 0.860,
    },
    "nviib": {
        "lo": 0.8501, "n2lo": -0.0071, "minimal": 0.0242,
        "d1": -0.014, "d1_error": 0.001,
        "d2": 0.006, "d2_error": 0.001, "total": 0.860,
    },
}

NORFOLK_MINIMAL_CONTACT_LECS = {
    "nvia": -0.000195,
    "nvib": -0.000560,
    "nviia": -0.000199,
    "nviib": -0.001080,
}


def regulated_ope_radial_functions(
    radius_fm: np.ndarray,
    *,
    pion_mass_fm: float,
    r_long_fm: float,
    ordering: str = "published",
) -> tuple[np.ndarray, np.ndarray]:
    """Return dimensionless OPE shapes with either regulator ordering.

    ``published`` implements Eq. (2.22), multiplying the already differentiated
    correlation functions by ``C_RL``. ``differentiate_regulated_yukawa`` first
    forms ``C_RL exp(-mu)/mu`` and then takes the radial Hessian. The latter is
    a diagnostic, not the prescription stated in the paper.
    """

    radius = np.asarray(radius_fm, dtype=np.float64)
    if np.any(radius <= 0.0) or pion_mass_fm <= 0.0 or r_long_fm <= 0.0:
        raise ValueError("radii, pion mass, and long-range cutoff must be positive")
    mu = pion_mass_fm * radius
    diffuseness = r_long_fm / 2.0
    regulator_argument = (radius / r_long_fm) ** 6 * np.exp(
        (radius - r_long_fm) / diffuseness
    )
    regulator = regulator_argument / (1.0 + regulator_argument)
    base_1 = -(1.0 + mu) * np.exp(-mu) / mu**3
    base_2 = (3.0 + 3.0 * mu + mu**2) * np.exp(-mu) / mu**3
    if ordering == "published":
        return regulator * base_1, regulator * base_2
    if ordering != "differentiate_regulated_yukawa":
        raise ValueError(f"unknown OPE regulator ordering {ordering!r}")

    logarithmic_derivative = (
        6.0 / radius + 1.0 / diffuseness
    ) / pion_mass_fm
    logarithmic_second = -6.0 / (radius * pion_mass_fm) ** 2
    regulator_prime = (
        regulator * (1.0 - regulator) * logarithmic_derivative
    )
    regulator_second = regulator * (1.0 - regulator) * (
        (1.0 - 2.0 * regulator) * logarithmic_derivative**2
        + logarithmic_second
    )
    yukawa = np.exp(-mu) / mu
    yukawa_prime = -(1.0 + mu) * np.exp(-mu) / mu**2
    yukawa_second = np.exp(-mu) * (
        1.0 / mu + 2.0 / mu**2 + 2.0 / mu**3
    )
    product_prime = regulator_prime * yukawa + regulator * yukawa_prime
    product_second = (
        regulator_second * yukawa
        + 2.0 * regulator_prime * yukawa_prime
        + regulator * yukawa_second
    )
    return product_prime / mu, product_second - product_prime / mu


def _spin_operators() -> tuple[np.ndarray, np.ndarray]:
    identity = np.eye(2, dtype=np.complex128)
    pauli = (
        np.asarray([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128),
        np.asarray([[0.0, -1j], [1j, 0.0]], dtype=np.complex128),
        np.asarray([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128),
    )
    sigma_1 = np.asarray([np.kron(matrix, identity) for matrix in pauli])
    sigma_2 = np.asarray([np.kron(identity, matrix) for matrix in pauli])
    return sigma_1, sigma_2


def _operator_dot(operators: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return np.einsum("iab,i->ab", operators, vector)


def _operator_cross(operators: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return np.asarray(
        [
            operators[1] * vector[2] - operators[2] * vector[1],
            operators[2] * vector[0] - operators[0] * vector[2],
            operators[0] * vector[1] - operators[1] * vector[0],
        ]
    )


def isoscalar_chiral_two_body_current(
    *,
    photon_momentum: np.ndarray,
    nucleon_1_transfer: np.ndarray,
    nucleon_2_transfer: np.ndarray,
    d9: float,
    l2: float,
    axial_coupling: float = 1.27,
    pion_decay_constant: float = 0.0924,
    pion_mass: float = 0.1380,
    electric_charge: float = 1.0,
    isospin_dot: float = -3.0,
) -> np.ndarray:
    """Return spatial current ``J[i, spin_out, spin_in]`` from Eq. (3).

    The input transfers must obey ``q1 + q2 = q``. No regulator is applied;
    callers must supply one consistently with their nuclear interaction.
    """

    q = np.asarray(photon_momentum, dtype=np.float64)
    q1 = np.asarray(nucleon_1_transfer, dtype=np.float64)
    q2 = np.asarray(nucleon_2_transfer, dtype=np.float64)
    if q.shape != (3,) or q1.shape != (3,) or q2.shape != (3,):
        raise ValueError("all momenta must be three-vectors")
    if not np.allclose(q1 + q2, q, rtol=1e-12, atol=1e-14):
        raise ValueError("nucleon transfers must sum to photon momentum")
    if pion_decay_constant <= 0.0 or pion_mass <= 0.0:
        raise ValueError("pion constants must be positive")

    sigma_1, sigma_2 = _spin_operators()
    pion_12 = (
        _operator_dot(sigma_2, q2)
        / (np.dot(q2, q2) + pion_mass**2)
    )[None, :, :] * np.cross(q1, q)[:, None, None]
    pion_21 = (
        _operator_dot(sigma_1, q1)
        / (np.dot(q1, q1) + pion_mass**2)
    )[None, :, :] * np.cross(q2, q)[:, None, None]
    long_range = (
        2j
        * electric_charge
        * axial_coupling
        * d9
        * isospin_dot
        / pion_decay_constant**2
        * (pion_12 + pion_21)
    )
    contact = (
        1j
        * electric_charge
        * l2
        * _operator_cross(sigma_1 + sigma_2, q)
    )
    return long_range + contact


def _coordinate_spin_angular_wave(
    direction: np.ndarray, u: float, w: float, projection: int = 1
) -> np.ndarray:
    """Return the coordinate-space S+D spin amplitude for fixed direction."""

    amplitude = np.zeros(4, dtype=np.complex128)
    for spin_1 in (0, 1):
        for spin_2 in (0, 1):
            index = 2 * spin_1 + spin_2
            amplitude[index] = (
                u
                / np.sqrt(4.0 * np.pi)
                * _triplet_spin_amplitude(projection, spin_1, spin_2)
            )
            for m_l, m_s, coefficient in _D_COUPLING[projection]:
                amplitude[index] += (
                    w
                    * coefficient
                    * _spherical_harmonic_l2(m_l, *direction)
                    * _triplet_spin_amplitude(m_s, spin_1, spin_2)
                )
    return amplitude


def _angular_quadratic_coefficients(
    operator, angular_order: int
) -> tuple[float, float, float]:
    """Integrate ``<psi|operator|psi>`` as ``a*u^2+b*u*w+c*w^2``."""

    values = []
    cos_nodes, cos_weights = np.polynomial.legendre.leggauss(angular_order)
    phi_nodes = 2.0 * np.pi * (np.arange(2 * angular_order) + 0.5) / (
        2 * angular_order
    )
    phi_weight = 2.0 * np.pi / len(phi_nodes)
    for u, w in ((1.0, 0.0), (0.0, 1.0), (1.0, 1.0)):
        integral = 0.0
        for cosine, theta_weight in zip(cos_nodes, cos_weights):
            sine = np.sqrt(max(0.0, 1.0 - cosine**2))
            for phi in phi_nodes:
                direction = np.asarray(
                    [sine * np.cos(phi), sine * np.sin(phi), cosine]
                )
                state = _coordinate_spin_angular_wave(direction, u, w)
                matrix = operator(direction)
                integral += (
                    theta_weight
                    * phi_weight
                    * np.vdot(state, matrix @ state).real
                )
        values.append(integral)
    return values[0], values[2] - values[0] - values[1], values[1]


def norfolk_n3lo_magnetic_moment(
    wave: RadialWaveFunction,
    *,
    model: str,
    angular_order: int = 18,
    ope_regulator_ordering: str = "published",
    axial_coupling: float = 1.29,
    pion_decay_constant_mev: float = 92.4,
    pion_mass_mev: float = 138.039,
    nucleon_mass_mev: float = 938.9,
    isoscalar_lecs: tuple[float, float] | None = None,
    include_ope_fourier_contact: bool = True,
) -> dict[str, float]:
    """Evaluate the matched Norfolk N3LO isoscalar magnetic operators.

    This contracts Eqs. (2.12), (2.14), and (2.15) of Schiavilla et al.,
    arXiv:1809.10180, with the stretched coordinate-space deuteron state.
    By default it also includes the regulated delta-function term generated
    by the OPE Fourier transform and explicitly retained in the authors'
    fitting code (Gnech, ``OPE_N3LO_fourier_transform.pdf``, July 2026).
    Returned values are in nuclear magnetons.
    """

    key = model.lower()
    if key not in NORFOLK_ISOSCALAR_LECS:
        raise ValueError(f"unknown Norfolk model {model!r}")
    if wave.representation != "coordinate":
        raise ValueError("Norfolk magnetic moment requires a coordinate wave function")
    if angular_order < 4:
        raise ValueError("angular_order must be at least four")

    r_short = 0.8 if key.endswith("a") else 0.7
    r_long = 1.2 if key.endswith("a") else 1.0
    d1, d2 = (
        NORFOLK_ISOSCALAR_LECS[key]
        if isoscalar_lecs is None
        else tuple(float(value) for value in isoscalar_lecs)
    )
    d1_min = NORFOLK_MINIMAL_CONTACT_LECS[key]
    hbarc = 197.3269804
    pion_mass_fm = pion_mass_mev / hbarc
    fpi_fm = pion_decay_constant_mev / hbarc

    sigma_1, sigma_2 = _spin_operators()
    sigma_sum = sigma_1 + sigma_2
    spin_coefficients = _angular_quadratic_coefficients(
        lambda _direction: sigma_sum[2], angular_order
    )
    tensor_coefficients = _angular_quadratic_coefficients(
        lambda direction: np.einsum("i,iab->ab", direction, sigma_sum)
        * direction[2],
        angular_order,
    )

    contact_density = np.zeros_like(wave.grid)
    ope_density = np.zeros_like(wave.grid)
    ope_i1_density = np.zeros_like(wave.grid)
    ope_i2_density = np.zeros_like(wave.grid)
    ope_fourier_contact_density = np.zeros_like(wave.grid)
    for radial_index, (radius, u, w) in enumerate(zip(wave.grid, wave.u, wave.w)):
        z = radius / r_short
        contact_c0 = np.exp(-(z**2)) / (
            np.pi**1.5 * (pion_mass_fm * r_short) ** 3
        )
        mu = pion_mass_fm * radius
        prefactor = (
            axial_coupling
            / (16.0 * np.pi)
            * pion_mass_fm**2
            / fpi_fm**2
            * d2
        )
        shape_1, shape_2 = regulated_ope_radial_functions(
            np.asarray([radius]),
            pion_mass_fm=pion_mass_fm,
            r_long_fm=r_long,
            ordering=ope_regulator_ordering,
        )
        i1 = prefactor * shape_1[0]
        i2 = prefactor * shape_2[0]
        # The July-2026 note prints d_1^S in its Eq. (8), but this delta term
        # comes from Fourier-transforming Eq. (1), which is proportional to
        # d_2^S.  Using d_2^S preserves operator linearity and reproduces all
        # four PRC106 Table-IV OPE entries, including the a/b sign reversal.
        i_contact = (
            -axial_coupling
            / 12.0
            * pion_mass_fm**2
            / fpi_fm**2
            * d2
            * contact_c0
            if include_ope_fourier_contact
            else 0.0
        )

        radial_products = np.asarray([u * u, u * w, w * w])
        contact_angular = np.dot(spin_coefficients, radial_products)
        ope_i1_angular = i1 * contact_angular
        ope_i2_angular = i2 * np.dot(tensor_coefficients, radial_products)
        ope_fourier_contact_angular = i_contact * contact_angular
        ope_angular = (
            ope_i1_angular + ope_i2_angular + ope_fourier_contact_angular
        )
        contact_density[radial_index] = contact_c0 * contact_angular
        ope_density[radial_index] = -3.0 * ope_angular
        ope_i1_density[radial_index] = -3.0 * ope_i1_angular
        ope_i2_density[radial_index] = -3.0 * ope_i2_angular
        ope_fourier_contact_density[radial_index] = (
            -3.0 * ope_fourier_contact_angular
        )

    magnetic_conversion = -2.0 * nucleon_mass_mev / pion_mass_mev
    contact_coefficient = magnetic_conversion * simpson(
        contact_density, x=wave.grid
    )
    ope = magnetic_conversion * simpson(ope_density, x=wave.grid)
    ope_i1 = magnetic_conversion * simpson(ope_i1_density, x=wave.grid)
    ope_i2 = magnetic_conversion * simpson(ope_i2_density, x=wave.grid)
    ope_fourier_contact = magnetic_conversion * simpson(
        ope_fourier_contact_density, x=wave.grid
    )
    return {
        "minimal_contact": d1_min * contact_coefficient,
        "nonminimal_contact": d1 * contact_coefficient,
        "ope": ope,
        "ope_i1": ope_i1,
        "ope_i2": ope_i2,
        "ope_fourier_contact": ope_fourier_contact,
        "ope_long_range": ope_i1 + ope_i2,
        "ope_unit_d2": (ope_i1 + ope_i2) / d2 if d2 != 0.0 else np.nan,
        "ope_i1_unit_d2": ope_i1 / d2 if d2 != 0.0 else np.nan,
        "ope_i2_unit_d2": ope_i2 / d2 if d2 != 0.0 else np.nan,
        "ope_fourier_contact_unit_d2": (
            ope_fourier_contact / d2 if d2 != 0.0 else np.nan
        ),
        "contact_unit_d1": contact_coefficient,
        "total": (d1_min + d1) * contact_coefficient + ope,
    }
