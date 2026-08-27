from deuteron_wigner.bridge import hqcdriquarkfixedkvradtail1 as c
def test_manifest():assert c.tail_program_manifest()["complete"]==8
def test_tail():
 rid=c.tail_program_manifest()["rows"][0]["radial_id"];p=c.tail_enclosure_program(rid,2)
 assert p["term_count"]==9 and p["cutoff_monotone_decreasing"] and p["limit_Q_infinity"]=="0"
def test_allocator():
 rid=c.tail_program_manifest()["rows"][0]["radial_id"];a=c.error_allocator(rid,0)
 assert a["missing_measure"]==0 and a["double_count_measure"]==0
def test_release():assert c.release_manifest()["tail_programs"]==8 and c.release_manifest()["assembled_matrix_elements"]==0
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkvradtail1_authority()["package_root"]==c.PACKAGE_ROOT
 assert all(c.mutate_live_hqcdriquarkfixedkvradtail1(i)["pass"] for i in range(384))
