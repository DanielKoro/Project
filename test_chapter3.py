import pytest
# from collections import namedtuple
# import tasks
# # Task element types : [summary: str, owner: str, done: bool, id: int]
# Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
# Task.__new__.__defaults__ = (None, None, False, None)
#


@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get @ pytest.mark.smoke
def test_get_raises():
    """get() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')
