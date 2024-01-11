import pytest
from structures.heap import MaxHeap


def test_bubble_up():
    heap = MaxHeap(10)
    heap._array = [20, 18, 15, 14, 12, 13, 3]
    heap._size = len(heap._array)
    assert heap.is_valid()

    heap._array = [20, 18, 15, 14, 12, 13, 3, 21]
    heap._size = len(heap._array)
    heap.bubble_up(8)
    assert heap.is_valid()


def test_bubble_down():
    heap = MaxHeap(10)
    heap._array = [5, 18, 15, 14, 12, 13, 3]
    heap._size = len(heap._array)
    heap.bubble_down(1)
    print(heap)
    assert heap.is_valid()


def test_insert():
    heap = MaxHeap(5)
    heap.insert(5)
    heap.insert(8)
    heap.insert(7)
    heap.insert(3)
    assert heap.max() == 8
    heap.insert(11)
    with pytest.raises(IndexError, match="Maximum heap size exceeded"):
        heap.insert(12)


def test_heap_remove():
    heap = MaxHeap(5)
    heap.insert(5)
    heap.insert(8)
    heap.insert(7)
    heap.insert(3)
    assert heap.max() == 8

    assert heap.remove() == 8
    assert heap.max() == 7
    assert heap.remove() == 7
    assert heap.max() == 5
    assert heap.remove() == 5
    assert heap.remove() == 3
    with pytest.raises(IndexError, match="Heap is empty"):
        heap.remove()


