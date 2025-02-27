import pytest
from stack import Stack


@pytest.fixture
def stack():
    return Stack()


def test_push(stack):
    stack.push(100)
    assert len(stack.items) == 1


def test_pop(stack):
    stack.push(200)
    assert stack.pop() == 200

    with pytest.raises(IndexError, match="Stack is empty."):
        stack.pop()


def test_peek(stack):
    stack.push(500)
    assert stack.peek() == 500

    stack.pop()
    with pytest.raises(IndexError, match="Stack is empty."):
        stack.peek()


def test_is_empty(stack):
    assert stack.is_empty() == True

    stack.push(1000)
    assert stack.is_empty() == False


def test_size(stack):
    assert stack.size() == 0

    stack.push(100)
    stack.push(200)
    assert stack.size() == 2

    stack.pop()
    assert stack.size() == 1
