from deuteron_wigner.bridge.ifcontact4.core import audit_public_inputs,STATUS
def test_c83_requires_authenticated_c82_pair_coordinate_import():
 x=audit_public_inputs();assert x['status']==STATUS and not x['C82_public_root_verified'] and not x['kernel_products_created']
