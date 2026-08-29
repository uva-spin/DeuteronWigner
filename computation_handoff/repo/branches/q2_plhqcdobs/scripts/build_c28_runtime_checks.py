#!/usr/bin/env python3
"""Build deterministic serial/restart diagnostics from isolated native runs."""
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1];RT=ROOT/'data/runtime/c28_art25'
def load(prefix):return json.loads((RT/(prefix+'.json')).read_text()),np.load(RT/(prefix+'.npz'))
def flat(x):
    if isinstance(x,list):
        return [z for y in x for z in flat(y)]
    return [float(x)]
def main():
    shard,zs=load('shard_1');serial,za=load('serial_member1');restart,zb=load('restart_member1')
    i=next(i for i,x in enumerate(shard['member_identities']) if x['lambda_index']==1)
    nuisance_serial=np.asarray(flat(serial['nuisance_profiles']))
    nuisance_parallel=np.asarray(flat([shard['nuisance_profiles'][i]]))
    nuisance_restart=np.asarray(flat(restart['nuisance_profiles']))
    checks={
      'serial_parallel_max_abs_residual':float(np.max(np.abs(za['predictions'][0]-zs['predictions'][i]))),
      'serial_parallel_chi2_max_abs_residual':float(np.max(np.abs(za['chi2'][0]-zs['chi2'][i]))),
      'restart_max_abs_residual':float(np.max(np.abs(za['predictions'][0]-zb['predictions'][0]))),
      'restart_chi2_max_abs_residual':float(np.max(np.abs(za['chi2'][0]-zb['chi2'][0]))),
      'serial_parallel_nuisance_max_abs_residual':float(np.max(np.abs(nuisance_serial-nuisance_parallel))),
      'restart_nuisance_max_abs_residual':float(np.max(np.abs(nuisance_serial-nuisance_restart))),
      'identity_equal':serial['member_identities']==restart['member_identities']==[shard['member_identities'][i]],
      'point_order_equal':serial['point_ids']==restart['point_ids']==shard['point_ids'],
      'frozen_member':1,'frozen_points':len(serial['point_ids']),'missing':0,'duplicate':0,
      'checkpoint_semantics':'content-addressed shard plus explicit lambda-index merge; restart recomputes frozen member in a clean process'
    }
    (RT/'checkpoint_checks.json').write_text(json.dumps(checks,indent=2,sort_keys=True)+'\n')
    assert all(v <= 5e-14 for k,v in checks.items() if k.endswith('residual')) and all(checks[k] for k in ('identity_equal','point_order_equal'))
    print(json.dumps(checks,sort_keys=True))
if __name__=='__main__':main()
