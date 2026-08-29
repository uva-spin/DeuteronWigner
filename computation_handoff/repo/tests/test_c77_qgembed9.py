import numpy as np
from deuteron_wigner.bridge.qgembed9 import core

def test_c77_embedding_is_executable_and_threshold_free():
    package=core.QGEmbeddingPackage(); x=package.load_canonical_tm_crosswalk()
    assert x['counts']['blocks']==733 and x['counts']['coefficients']==171153
    assert sum(x['counts']['cm_ground'].values())==733
    assert x['orientation'].endswith('adapter=identity')
    for r in core.RESOLUTIONS:
        a=package.load_qg_embedding_package(r.label); assert a['shape'][1]//4==x['counts']['cm_ground'][r.label]
        v=np.ones(a['shape'][1],complex); assert np.linalg.norm(package.embed_physical_qg_to_raw(r.label,v)['value'])>0
    assert core.validate_package()['pass']
