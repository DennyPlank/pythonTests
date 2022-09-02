from operator import attrgetter
import pytest
from stuff.accum import Accumulator

# Fixtures should always return a value
@pytest.fixture 
def accum():
    return Accumulator()

@pytest.fixture 
def accum2():
    return Accumulator()

def test_accum_init(accum):
    assert accum.count == 0

def test_accum_add_one(accum2):
    accum2.add()
    assert accum2.count == 1

def test_accum_init(accum):
    accum.add(3)
    assert accum.count == 3

def test_accum_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10
