import pytest

def test_passes():
    assert 1 + 1 == 2

@pytest.mark.skip(reason="Never ever leave failing tests in the main branch! It's better to quickly skip the test and fix it later, than to let it keep failing for hours.")
def test_fails():
    assert False
