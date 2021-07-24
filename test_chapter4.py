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


@pytest.fixture()
def create_four_tasks(tasks_db):
    tasks_two = tasks.Task(summary="hummus", owner="Daniel", done="yes")
    tasks.add(tasks_two)
    tasks_three = tasks.Task(summary="onion", owner="pytestmaster", done="almost")
    tasks.add(tasks_three)
    tasks_four = tasks.Task(summary="avacado", owner="many", done="sorta")
    tasks.add(tasks_four)
    tasks_five = tasks.Task(summary="alligator", owner="fedor", done="quite")
    tasks.add(tasks_five)
    yield
    tasks.delete_all()


@pytest.fixture()
def more_tasks(tasks_db):
    tasks_1 = tasks.Task(summary="none", owner="none", done=False, id="none")
    tasks.add(tasks_1)
    tasks_2 = tasks.Task(summary="none", owner="none", done=False, id="none")
    tasks.add(tasks_2)
    yield
    tasks.delete_all()


def test_list_tasks(create_four_tasks):
    tasks_list = tasks.list_tasks()
    assert len(tasks_list) == 4


def test_list_tasks2(create_four_tasks):
    tasks_list = tasks.list_tasks()
    assert "Daniel" in [task.owner for task in tasks_list]


def test_list_tasks3(create_four_tasks):
    tasks_list = tasks.list_tasks()
    assert len(tasks_list) * 2 == 8


def test_count2(tasks_db):
    # TODO: Create fixture similar to "four_tasks" but to creat and removes 2 tasks and use it here
    tasks_1 = tasks.Task(summary="none", owner="none", done=False)
    tasks.add(tasks_1)

    tasks_2 = tasks.Task(summary="any value", owner="Daniel", done=False)
    tasks.add(tasks_2)
    expected = 2
    actual = tasks.count()
    assert actual == expected
    tasks.delete_all()
    tasks.list_tasks()


class MyClass: # Here you create a class
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr13 = attr3


my_class_instance = MyClass(1, 2, 3)  # Here you create an instance of the class
my_class_instance2 = MyClass(attr1=1, attr2=2, attr3=3)  # Here you create an instance of the class


def my_func_with_args(arg1, arg2, arg3):  # Here we define a function
    print(arg1, arg2, arg3)


def delete_everything():
    """
    If you cal me I will delete all
    """
    pass


my_func_with_args(1, 2, 3)  # Here you call the function
my_func_with_args(arg2=2, arg1=1, arg3=3)  # Here you call the function

delete_everything()  # Here you call the function and it does the work you need
delete_everything  # Here you just mentioned function but it does nothing


def my_func():
    return "I am called"


print(my_func)  # Here I am printing function

print(my_func())  # Here I am calling function and printing what the function has returned to me. The "()" == "Hey function I am alling you 🚨"


