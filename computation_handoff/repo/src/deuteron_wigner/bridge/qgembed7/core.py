"""C73 fail-closed C72 public-object gate."""
from ..qgcolor5.core import TripletAuthorityPackage
STATUS='C73_QGEMBED_C72_IMPORT_INCOMPLETE';NEXT='C74/QGCOLOR6 — immutable C72 basis/status/exact-record/bound loaders and strict numerical loading'
def preflight():
 p=TripletAuthorityPackage();missing=[x for x in ('load_basis','load_statuses','load_exact_records','load_bounds') if not hasattr(p,x)]
 return {'status':STATUS,'next':NEXT,'C72_objects':len(p.index['objects']),'C72_records':len(p.index['records']),'missing_public_loaders':missing,'strict_allow_pickle_false':False,'blocker':'C72 authenticates its index but its public package has no immutable basis/status/exact-record/bound loaders and numerical load omits allow_pickle=False; C73 cannot infer those identities from private index fields or array positions.','no_embedding':True,'no_contact':True}
