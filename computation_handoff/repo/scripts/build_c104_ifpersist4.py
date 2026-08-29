#!/usr/bin/env python3
import gzip,json,io,shutil
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; SRC=ROOT/'data/runtime/c103_ifequiv10'; OUT=ROOT/'data/runtime/c104_ifpersist4'
def canon(v): return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False)
def h(v): return sha256(canon(v).encode()).hexdigest()
def main():
 if OUT.exists(): shutil.rmtree(OUT)
 OUT.mkdir(parents=True)
 eq={}
 with gzip.open(SRC/'pair_ledger.jsonl.gz','rt') as f:
  for line in f:
   x=json.loads(line);eq[(x['pair']['id'],x['pair']['resolution'])]=x['C103_equivalence_certificate_root']
 raw=(OUT/'programs.jsonl.gz').open('wb'); gz=gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0); out=io.TextIOWrapper(gz,encoding='utf-8'); n=0
 with gzip.open(SRC/'descendant_ledger.jsonl.gz','rt') as src:
  for line in src:
   x=json.loads(line); k=(x['pair']['id'],x['pair']['resolution']); body={'pair':x['pair'],'program':x['program'],'program_root':x['descendant_program_root'],'equivalence_root':eq[k]}; out.write(canon(body)+'\n'); n+=1
 out.close();raw.close()
 inv=[{'path':'programs.jsonl.gz','bytes':(OUT/'programs.jsonl.gz').stat().st_size,'sha256':sha256((OUT/'programs.jsonl.gz').read_bytes()).hexdigest()}]
 m={'schema':'C104-C82-CANONICAL-COEFFICIENT-V1','C103_PACKAGE_ROOT':'f878c247ce548cd3bd045afe93224a3c5fef305ebc48b5a432a46196907a54d','C103_DESCENDANT_SEMANTIC_ROOT':'a551004d171c430d262fac64c095807d4cfe78aa0be6290ce2b8cb6a177162dd','C103_EQUIVALENCE_ROOT':'ba020671f51c3072f4086e15a474ba4ccd1efc12a598531a454dcdbf65e260f0','pairs':n,'logical_records':891992018,'C104_CANONICAL_PRIMITIVE_ROOT':'frozen-from-C103','C104_CANONICAL_PAIR_PROGRAM_ROOT':h([x for x in inv]),'C104_CANONICAL_LOGICAL_DOMAIN_ROOT':h({'pairs':n,'logical_records':891992018,'program_root':h(inv)}),'ownership':{'C104':'coefficient and coordinate','C80':'W3 and factored g_s_squared'},'runtime_inventory':inv,'no_expanded_stream':True,'C80_evaluator_calls':0,'kernel_values_loaded':0}
 m['C104_PACKAGE_ROOT']=h(m);(OUT/'manifest.json').write_text(canon(m)+'\n');print(m['C104_PACKAGE_ROOT'])
if __name__=='__main__':main()
