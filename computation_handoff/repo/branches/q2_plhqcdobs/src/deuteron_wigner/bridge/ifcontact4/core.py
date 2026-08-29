"""C83 fail-closed audit: C82 lacks an authenticated persisted import API."""
from hashlib import sha256
import inspect,json
from ..ifagg.core import IFContactAggregationBridge
from ..ifkernel2.core import ContactKernelPackage
STATUS='C83_IFCONTACT_SHARED_COORDINATE_INCOMPLETE'
NEXT='C84/IFCOORD2 — create an authenticated immutable C82 runtime loader for persisted pair-coordinate records before any product'
BLOCKER='C83.C82.AUTHENTICATED_PERSISTED_PAIR_COORDINATE_IMPORT'
def audit_public_inputs():
 c80=ContactKernelPackage(); source=inspect.getsource(IFContactAggregationBridge.__init__)
 missing=('root.json verification' not in source and 'index.json verification' not in source and 'data/runtime/c82_ifagg' not in source)
 if not missing: raise RuntimeError('C82 interface changed; re-audit required')
 return {'status':STATUS,'next':NEXT,'blocker':BLOCKER,'C80_public_root':c80.input_freeze()['status'],'C82_runtime_exists':True,'C82_public_root_verified':False,'C82_persisted_pair_records':False,'reason':'C82 public constructor regenerates bridge state from C77/C74 APIs and exposes lazy computed records; it does not authenticate C82 root/index or load immutable persisted pair-coordinate coefficient records.','matrix_created':False,'kernel_products_created':False}
