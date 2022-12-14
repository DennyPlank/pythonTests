from operator import attrgetter
import pytest
from stuff.accum import Accumulator

# Fixtures should always return a value
@pytest.fixture 
def accum():
    return Accumulator()

# Below is an example of yielding (ln 13), which acts as a santizer (python generator)
# @pytest.fixture 
# def accum():
#     yield Accumulator()

def test_accum_init(accum):
    assert accum.count == 0

def test_accum_add_one(accum):
    accum.add()
    assert accum.count == 1

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
