"""
this module contains basic unit test for stack operation
"""

import pytest
from libs.stack import Stack

@pytest.fixture
def stac():
    return Stack()

@pytest.mark.stack
def test_stack_init(stac):
    assert stac.length() == 0

@pytest.mark.stack
def test_stack_add_one(stac):
    stac.add(10)
    assert stac.length() == 1

@pytest.mark.stack
def test_stack_add_more_than_one(stac):
    stac.add([20, 30, 40])
    assert stac.length() == 3

@pytest.mark.stack
def test_stack_without_add(stac):
    with pytest.raises(AssertionError, match=r'bound method') as e:
        assert stac.length == 10

@pytest.mark.stack
def test_remove_from_stack(stac):
    stac.add([10,20,30])
    stac.remove(20)
    stac.remove(10)
    assert stac.length() == 1