"""C74 safe public interface for unchanged authenticated C72 authority."""
from pathlib import Path
from types import MappingProxyType
import json,numpy as np
from ..qgcolor5.core import ROOT,R,fh,TripletAuthorityPackage as C72
STATUS='C74_SOURCE_DERIVED_TRIPLET_PUBLIC_IMPORT_READY'
class TripletAuthorityPackage:
 def __init__(self):
  self._c72=C72();self._index=MappingProxyType(self._c72.index);self._records=tuple(MappingProxyType(dict(x)) for x in self._index['records']);self._rows=tuple(self._index['rows']);self._columns=tuple(self._index['columns'])
 def product_rows(self):return self._rows
 def triplet_columns(self):return self._columns
 def pair_identities(self):return tuple((x['row_id'],x['column_id']) for x in self._records)
 def statuses(self):return tuple(x['status'] for x in self._records)
 def exact_records(self):return self._records
 def bounds(self):return tuple(MappingProxyType({'row_id':x['row_id'],'column_id':x['column_id'],'bound':x['bound'],'array':x['array'],'index':tuple(x['index']),'dtype':x['dtype'],'precision':x['precision'],'interval':x['interval']}) for x in self._records)
 def load(self,id):
  o=next(x for x in self._index['objects'] if x['id']==id);p=(ROOT/o['path']).resolve()
  if R not in p.parents or p.is_symlink():raise ValueError('unsafe runtime path')
  a=np.load(p,allow_pickle=False)
  if a.dtype.hasobject or fh(p)!=o['sha256']:raise ValueError('unsafe/mismatched authority array')
  a.setflags(write=False);return a
