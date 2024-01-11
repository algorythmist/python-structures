from typing import Any


class MaxHeap:

    def __init__(self, max_size):
        self._array = [None] * (max_size+1)
        self._size = 0
        self._max_size = max_size

    def __len__(self):
        return self._size

    def max(self):
        if len(self) == 0:
            return None
        return self._array[1]

    def parent(self, index: int) -> int:
        return index // 2

    def left(self, parent: int) -> int:
        return 2 * parent

    def right(self, parent: int) -> int:
        return 2 * parent + 1

    def is_valid(self):
        for i in range(self._size, 2, -1):
            if self._array[self.parent(i)] < self._array[i]:
                return False
        return True

    def insert(self, item: Any):
        if self._size == self._max_size:
            raise IndexError("Maximum heap size exceeded")
        self._size += 1
        self._array[self._size] = item
        self.bubble_up(self._size)

    def remove(self) -> Any:
        if self._size == 0:
            raise IndexError("Heap is empty")
        value = self._array[1]
        self._array[1] = self._array[self._size]
        self._size -= 1
        self.bubble_down(1)
        return value

    def bubble_up(self, index: int):
        while index > 1 and self._array[self.parent(index)] < self._array[index]:
            parent_index = self.parent(index)
            self.swap(parent_index, index)
            index = parent_index

    def bubble_down(self, index: int):
        left_child = self.left(index)
        right_child = self.right(index)
        max_child = self.max_index(left_child, right_child)
        if not max_child:
            return
        if self._array[index] < self._array[max_child]:
            self.swap(max_child, index)
            self.bubble_down(max_child)

    def max_index(self, i, j):
        if i <= self._size and j <= self._size:
            return j if self._array[i] < self._array[j] else i
        if i <= self._size:
            return i
        if j <= i <= self._size:
            return j
        return None

    def swap(self, i, j):
        self._array[i], self._array[j] = self._array[j], self._array[i]





