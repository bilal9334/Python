import pytest
from todolist import ToDoList


@pytest.fixture
def todolist():
    return ToDoList()


def test_add_task(todolist):
    todolist.add_task("Make Coffee.")
    assert len(todolist.tasks) == 1


def test_remove_task(todolist):
    todolist.add_task("Make Coffee.")
    todolist.remove_task("Make Coffee.")
    assert todolist.get_tasks() == []

    with pytest.raises(ValueError, match="Task not found."):
        todolist.remove_task("Non-existent task")


def test_non_existent_task(todolist):
    with pytest.raises(ValueError, match="Task not found."):
        todolist.remove_task("Read a book")


def test_get_task(todolist):
    todolist.add_task("Read a book")
    todolist.add_task("Go jogging")
    assert todolist.get_tasks() == ["Read a book", "Go jogging"]
