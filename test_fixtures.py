import pytest


@pytest.fixture()
def daniel():
    """
    The goal of this fixture is to return some data we will use in test cases
    :return:
    """
    data = {"name": "Daniel", "second_name": "Korobok", "title": "Senior QA"}
    return data


def test_one(daniel):
    expected = "Senior QA"
    actual = daniel["title"]
    assert actual == expected


@pytest.fixture(scope= 'module')
def func_scope ():





# Pytest fixture - is a python function wrapped by @pytest.fixture decaorator. The pytest fixture provides data to tests we run.


"""
# Questions to you:
# 1.  What is python decorator ? (It always looks like @<function_name>)
@<func_or_class_name>
@<func_or_class_name>
@<func_or_class_name>
def some_function:
    pass
"""
