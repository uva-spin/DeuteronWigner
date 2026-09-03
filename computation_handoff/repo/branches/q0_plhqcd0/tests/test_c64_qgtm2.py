import json
from pathlib import Path
import numpy as np
import pytest

from deuteron_wigner.bridge.qgtm2 import core


@pytest.fixture(scope='session')
def bundle(tmp_path_factory):
    root = tmp_path_factory.mktemp('c64_qgtm2') / 'bundle'
    return root, core.materialize(root, clean=True)


def test_c64_complete_read_only_artifact_closure(bundle):
    root, index = bundle
    assert index['status'] == core.STATUS
    core.validate_index_contract(index)
    assert len(index['blocks']) == 733
    assert core.validate_bundle(root)['status'] == 'PASS'
    support = core.load_tm_block_support(index['blocks'][0]['block_id'], root)
    assert support['array'].flags.writeable is False
    action = core.apply_tm_block(index['blocks'][0]['block_id'], np.ones(index['blocks'][0]['shape'][1]), root)
    assert action['value'].flags.writeable is False


@pytest.mark.parametrize('fault_id', range(256))
def test_c64_focused_contract_mutations_are_detected(bundle, fault_id):
    _root, index = bundle
    mutated = core.mutate_live_c64(index, fault_id)
    assert mutated != index
    with pytest.raises(ValueError):
        core.validate_index_contract(mutated)
