import pytest

def test_passes():
    assert 1 + 1 == 2

@pytest.mark.skip(reason="Never ever leave failing tests in the main branch!")
def test_fails():
    """Failing tests in the main branch block any other changes!
    
    If you can't quickly fix a failing test, it's better to mark it skipped and come back later, than to let it keep failing for hours.
    """
    assert False
