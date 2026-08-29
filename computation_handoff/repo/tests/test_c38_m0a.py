from deuteron_wigner.bridge import m0a
def test_c38_probe_is_nonhadronic_and_normalized():
 q,qg,w,x=m0a.infrastructure(); assert q.norm==qg.norm==1 and w.transverse_closure and x.number_moment()==1
