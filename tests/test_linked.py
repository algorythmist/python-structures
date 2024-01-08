from structures.lists import *


def test_singly_linked_list():
    ll = LinkedList()
    assert ll.is_empty()
    assert len(ll) == 0

    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert len(ll) == 3
    assert ll[0] == 3
    assert ll[1] == 2

    ll.delete_head()
    assert len(ll) == 2

    ll.insert(4)
    ll.insert(5)

    ll.delete(2)
    assert len(ll) == 3
    elements = []
    ll.traverse(lambda x: elements.append(x))
    assert elements == [5, 4, 1]


def test_doubly_linked_list():
    stack = DoublyLinkedList()
    assert stack.is_empty()
    assert len(stack) == 0

    stack.prepend(1)
    stack.prepend(2)
    stack.prepend(3)

    assert stack.peek_first() == 3
    assert stack.peek_last() == 1
    assert stack.remove_first() == 3
    assert stack.remove_first() == 2
    assert stack.peek_first() == 1

    queue = DoublyLinkedList()
    assert queue.is_empty()
    assert len(queue) == 0

    queue.append(1)
    queue.append(2)
    queue.append(3)

    assert queue.peek_first() == 1
    assert queue.peek_last() == 3
    assert queue.remove_last() == 3
    assert queue.remove_last() == 2

    queue.append(4)
    queue.append(5)
    queue.append(6)
    queue.append(7)
    assert queue[1] == 4
    assert queue[3] == 6