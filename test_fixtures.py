import pytest

@pytest.fixture()
def test_somedata(test_somedata):
    assert test_somedata == (1, 2, 3, 4)
    print (my_fixture)

@pytest.fixture(scope= 'module')
def func_scope ():




