from typing import Any, Callable


class LinkedList:
    class LinkedListNode:

        def __init__(self, value: Any):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, index: int) -> Any:
        if index >= len(self):
            raise IndexError("Index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def insert(self, value: Any):
        node = LinkedList.LinkedListNode(value)
        node.next = self.head
        self.head = node
        self._size += 1

    def delete(self, index: int) -> Any:
        if index >= len(self):
            raise IndexError("Index out of range")

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        self._size -= 1

    def traverse(self, callback: Callable[[Any], None]):
        current = self.head
        while current:
            callback(current.value)
            current = current.next

    def delete_head(self) -> Any:
        return self.delete(0)

    def is_empty(self):
        return len(self) == 0


class DoublyLinkedList:
    class LinkedListNode:
        def __init__(self, value: Any):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, index: int) -> Any:
        if index >= len(self):
            raise IndexError("Index out of range")
        if index//2 <= self._size:
            current = self.head
            for i in range(index):
                current = current.next
            return current.value
        else:
            current = self.tail
            for i in range(index, 0, -1):
                current = current.prev
            return current.value

    def is_empty(self):
        return len(self) == 0

    def prepend(self, value: Any):
        node = DoublyLinkedList.LinkedListNode(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1

    def append(self, value: Any):
        node = DoublyLinkedList.LinkedListNode(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._size += 1

    def remove_first(self) -> Any:
        if self.is_empty():
            raise IndexError("List is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return value

    def remove_last(self) -> Any:
        if self.is_empty():
            raise IndexError("List is empty")
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return value

    def peek_first(self) -> Any:
        if self.is_empty():
            raise IndexError("List is empty")
        return self.head.value

    def peek_last(self) -> Any:
        if self.is_empty():
            raise IndexError("List is empty")
        return self.tail.value


class Stack:

    def __init__(self):
        self._dll = DoublyLinkedList()

    def push(self, item: Any):
        self._dll.prepend(item)

    def pop(self):
        self._dll.remove_first()

    def peek(self):
        self._dll.peek_first()


class Queue:

    def __init__(self):
        self._dll = DoublyLinkedList()

    def add(self, item: Any):
        self._dll.append(item)

    def remove(self):
        self._dll.remove_last()

    def peek(self):
        self._dll.peek_last()