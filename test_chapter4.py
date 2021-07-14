import pytest
from collections import namedtuple
from tasks_proj.src import tasks



@pytest.fixture()
def tasks_db():

    tasks.start_tasks_db(str(), 'tiny')
    yield

    tasks.stop_tasks_db()




@pytest.fixture()
def my_fixture():
    return 4


def test_count(my_fixture):
    assert my_fixture == 4
    print(my_fixture)

def test_count2():

    print(tasks.count())
