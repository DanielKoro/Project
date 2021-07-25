import pytest


def one():
    return 1


def test_one():
    """
    This test expect success
    """
    expected = 1
    actual = one()
    assert actual == expected


class DanielPracticeError(Exception):
    pass


# In this function error_we_raise=None specifies default value for the argument.
# So in case you call it like this failing_function() - without argument, the value of "error_we_raise" will be None.
def failing_function(error_we_raise=None):
    if error_we_raise == TypeError:
        raise TypeError
    elif error_we_raise == DanielPracticeError:
        raise DanielPracticeError
    else:
        raise Exception


def test_failing_function():

    with pytest.raises(TypeError): # Here we say, "hey pytest, you hould expect the error of type I specified as argument"
        # You need to call the function we are testing so it raises the exception we expect
        failing_function(TypeError)

    with pytest.raises(DanielPracticeError):
        failing_function(DanielPracticeError)

    with pytest.raises(Exception):
        failing_function(Exception)



