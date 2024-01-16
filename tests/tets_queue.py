from structures.lists import Queue


def test_queue():
    queue = Queue()
    queue.add('A')
    assert queue.peek() == 'A'
    label = queue.remove()
    assert label == 'A'
    assert len(queue) == 0

