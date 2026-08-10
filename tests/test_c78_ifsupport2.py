from deuteron_wigner.bridge.ifsupport2 import core
def test_c78_support_is_symbolic_and_ordered():
 p=core.IFermContactSupportPackage();v=core.validate_package();assert v['pass'] and v['focused_live_mutations']>=320
 for r in core.RESOLUTIONS:
  x=p.load_iferm_contact_support_package(r.label);w=p.contact_witnesses(x['emission_edges'][0]['physical_qg_id'],x['absorption_edges'][0]['physical_qg_id'],r.label)[0]
  assert p.contact_support_status(w['physical_bra_id'],w['physical_ket_id'],r.label)=='NONZERO_SYMBOLIC_CONTACT_KERNEL_SUPPORT'
  assert p.contact_symbolic_coefficients(w['physical_bra_id'],w['physical_ket_id'],r.label)[0]['numerical_value']=='NOT_EVALUATED'
