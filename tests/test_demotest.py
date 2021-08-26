import pytest

def simple_add(): 
    return 1 + 1

def test_addition(): 
    z = simple_add()
    assert z == 2