import pytest
from collections import namedtuple
from tasks_proj.src import tasks



@pytest.fixture()
def tasks_db():
    tasks.start_tasks_db(db_path=".", db_type='tiny')
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def my_fixture():
    return 4


def test_count(my_fixture):
    assert my_fixture == 4
    print(my_fixture)


class MyClass: # Here you create a class
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr13 = attr3


my_class_instance = MyClass(1, 2, 3)  # Here you create an instance of the class
my_class_instance2 = MyClass(attr1=1, attr2=2, attr3=3)  # Here you create an instance of the class


def my_func_with_args(arg1, arg2, arg3):  # Here we define a function
    print(arg1, arg2, arg3)


my_func_with_args(1, 2, 3)  # Here you call the function
my_func_with_args(arg2=2, arg1=1, arg3=3)  # Here you call the function


def my_func():
    return "I am called"


print(my_func)  # Here I am printing function

print(my_func())  # Here I am calling function and printing what the function has returned to me. The "()" == "Hey function I am alling you 🚨"


def test_count2(tasks_db):

    #TODO: Create task instance (use class Task)
    tasks_one = tasks.Task(summary="Some tasks summary", owner="Alex", done=False)

    tasks.add(tasks_one)
    tasks_two = tasks.Task(summary="any value", owner="Daniel", done=True)
    tasks.add(tasks_two)

    tasks.delete

    expected = 2
    actual = tasks.count()
    # TODO: Make this test pass !!! Fine a way to clean all up after each test run
    assert actual == expected
