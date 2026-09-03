#!/usr/bin/env python3
import json
from pathlib import Path
from deuteron_wigner.bridge import m0a
def main():
 d=Path(__file__).resolve().parents[1]/'docs/next_level'; q,_,w,x=m0a.infrastructure(); assert x.number_moment()==1 and w.transverse_closure
 assert json.loads((d/'c38_injection_manifest.json').read_text())['count']>=3040
 assert json.loads((d/'c38_c39_prerequisite_gate.json').read_text())['status']==m0a.READY
 print('C38_VALIDATION_PASS')
if __name__=='__main__':main()
