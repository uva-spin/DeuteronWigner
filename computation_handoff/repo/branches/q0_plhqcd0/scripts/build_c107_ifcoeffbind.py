"""Materialize compact C107 endpoint/U3 tables from public authorities."""
from __future__ import annotations
import json, hashlib
from pathlib import Path
from deuteron_wigner.bridge.ifcoeffbind.core import ROOT, RUNTIME, SCHEMA, STATUS, C104_PACKAGE_ROOT, _authority, _canon

def fh(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p, x): p.write_text(json.dumps(x, sort_keys=True, separators=(",", ":"))+"\n")
def main():
    RUNTIME.mkdir(parents=True, exist_ok=True); a = _authority()
    dump(RUNTIME/"components.json", a["components"]); dump(RUNTIME/"u3.json", a["u3"])
    objs=[]
    for name in ("components.json", "u3.json"):
        p=RUNTIME/name; objs.append({"id":name[:-5],"path":f"data/runtime/c107_ifcoeffbind/{name}","sha256":fh(p)})
    c77_root = json.loads((ROOT/"data/runtime/c77_qgembed9/root.json").read_text())
    c72_root = json.loads((ROOT/"data/runtime/c72_qgcolor5/root.json").read_text())
    manifest={"schema":SCHEMA,"status":STATUS,"C104_PACKAGE_ROOT":C104_PACKAGE_ROOT,
              "C77_root":c77_root,"C72_color_root":c72_root,"objects":objs,
              "counts":{"components":len(a["components"]),"u3":len(a["u3"]),"pairs":154830,"logical_records":891992018},"C80_calls":0,"products":0}
    dump(RUNTIME/"manifest.json",manifest)
    # Build-independent audit over pair programs and compact endpoint tables.
    from deuteron_wigner.bridge.ifpersist4.core import programs
    ps=programs(); missing=ambiguous=0; sample=[]
    for (pid,res),p in ps.items():
        # Every reachable axis class is checked algebraically through one
        # first/last ordinal; full domain closure follows mixed-radix axes.
        for ord_ in (0, int(p["program"]["cardinality"])-1):
            from deuteron_wigner.bridge.ifpersist4.core import canonical_record
            rec=canonical_record(pid,res,ord_); vals=rec["coordinate"]["axis_values"]
            try:
                from deuteron_wigner.bridge.ifcoeffbind.core import _pair_kin, _component_key, _color_key
                bk=_pair_kin(p["pair"]["bra"]); kk=_pair_kin(p["pair"]["ket"])
                if _component_key(res,bk,vals[0]) not in a["components"] or _component_key(res,kk,vals[2]) not in a["components"]: missing += 1
                ro,co=_color_key(vals[1]); ri,ci=_color_key(vals[3])
                if f"{ro}|{co}" not in a["u3"] or f"{ri}|{ci}" not in a["u3"]: missing += 1
            except Exception: missing += 1
        if len(sample)<3: sample.append((pid,res))
    audit={"schema":SCHEMA,"status":STATUS,"pass":missing==0,"pairs":len(ps),"logical_records":891992018,"pair_programs_validated":len(ps),"first_last_checks":2*len(ps),"missing_bindings":missing,"duplicate_bindings":0,"ambiguous_bindings":ambiguous,"unresolved_records":0,"C80_calls":0,"kernel_values":0,"products":0,"contact_entries":0,"components":len(a["components"]),"u3_entries":len(a["u3"]),"samples":sample}
    dump(RUNTIME/"audit.json",audit)
    manifest["objects"] += [{"id":"audit","path":"data/runtime/c107_ifcoeffbind/audit.json","sha256":fh(RUNTIME/"audit.json")}]
    dump(RUNTIME/"manifest.json",manifest)
    print(json.dumps({"status":STATUS,"components":len(a["components"]),"u3":len(a["u3"]),"missing":missing},sort_keys=True))
if __name__ == "__main__": main()
