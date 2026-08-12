"""Compact key-to-line transport for frozen C97 operand shards."""
from __future__ import annotations
import gzip
from hashlib import sha256
import json
from pathlib import Path
import struct
from types import MappingProxyType
from typing import Any
from .zran_runtime import PersistentZranReader, _sha_file

MAGIC=b"C97PIXI1"; HEADER=128; ENTRY=struct.Struct(">32sQI32s32sQI")
def canonical(v: Any)->bytes: return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=True,allow_nan=False).encode()
def key(resolution:str,pair_id:str)->bytes: return sha256(b"C97_PROOF_INPUT\0"+canonical({"resolution":resolution,"pair_id":pair_id})).digest()

def build(source:Path, output:Path, zran:MappingProxyType)->MappingProxyType:
    rows=[]; offset=0; count=0
    with gzip.open(source,"rb") as stream:
        for raw in stream:
            rec=json.loads(raw); pair=rec["pair"]; rows.append(ENTRY.pack(key(pair["resolution"],pair["id"]),offset,len(raw),sha256(raw).digest(),bytes.fromhex(rec["proof_input_root"]),pair["global_sequence"],pair["resolution_sequence"])); offset+=len(raw);count+=1
    rows.sort(key=lambda r:r[:32])
    if any(a[:32]==b[:32] for a,b in zip(rows,rows[1:])): raise ValueError("duplicate C97 proof-input key")
    header=bytearray(HEADER);header[:8]=MAGIC;struct.pack_into(">IIQ",header,8,1,ENTRY.size,count);header[24:56]=bytes.fromhex(_sha_file(source));header[56:88]=bytes.fromhex(zran["root"])
    table=b"".join(rows);header[88:120]=sha256(table).digest();tmp=output.with_suffix(output.suffix+".tmp");tmp.write_bytes(bytes(header)+table);tmp.replace(output)
    body={"schema":"C97-PROOF-INPUT-INDEX-V1","records":count,"source_sha256":_sha_file(source),"zran_root":zran["root"],"table_sha256":sha256(table).hexdigest(),"index_sha256":_sha_file(output),"index_name":output.name}
    body["root"]=sha256(canonical(body)).hexdigest();output.with_suffix(output.suffix+".json").write_text(json.dumps(body,sort_keys=True,separators=(",",":"))+"\n");return MappingProxyType(body)

class Reader:
    def __init__(self,source:Path,index:Path,zran:PersistentZranReader):
        self.source=source; self.zran=zran; self.manifest=MappingProxyType(json.loads(index.with_suffix(index.suffix+".json").read_text()));raw=index.read_bytes()
        if raw[:8]!=MAGIC or _sha_file(source)!=self.manifest["source_sha256"] or zran.metadata["root"]!=self.manifest["zran_root"] or _sha_file(index)!=self.manifest["index_sha256"] or sha256(raw[HEADER:]).hexdigest()!=self.manifest["table_sha256"]:raise ValueError("C97 proof-input index authentication failure")
        self.table=raw[HEADER:]
    def lookup(self,resolution:str,pair_id:str)->MappingProxyType:
        d=key(resolution,pair_id);lo=0;hi=self.manifest["records"]
        while lo<hi:
            m=(lo+hi)//2
            if self.table[m*ENTRY.size:m*ENTRY.size+32]<d:lo=m+1
            else:hi=m
        if lo>=self.manifest["records"] or self.table[lo*ENTRY.size:lo*ENTRY.size+32]!=d:raise KeyError(pair_id)
        _,off,n,line_sha,root,gseq,lseq=ENTRY.unpack_from(self.table,lo*ENTRY.size);raw=self.zran.read_uncompressed_range(off,n)
        rec=json.loads(raw)
        if sha256(raw).digest()!=line_sha or rec["pair"]["id"]!=pair_id or rec["pair"]["resolution"]!=resolution or rec["pair"]["global_sequence"]!=gseq or rec["pair"]["resolution_sequence"]!=lseq or rec["proof_input_root"]!=root.hex():raise ValueError("C97 proof-input line identity mismatch")
        return MappingProxyType(rec)
    def close(self)->None:self.zran.close()
