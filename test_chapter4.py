import pytest
from collections import namedtuple
from tasks_proj.src import tasks


def test_practise():
    assert (1, 2, 3) == (1, 2, 3)

@pytest.mark.xfail()
def test_practise1():
    assert (1, 2, 3) == (3, 2, 1)


def test_practise2():
    assert (1, 2, 3, 4) == (4, 3, 2, 1)