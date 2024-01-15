import hashlib
from abc import ABC
from typing import Any

from structures.lists import LinkedList


class Hashtable(ABC):

    def __getitem__(self, key: Any):
        pass

    def __setitem__(self, key: Any, value: Any):
        pass

    def __contains__(self, key: Any) -> bool:
        pass

    def __delitem__(self, key: Any) -> bool:
        pass


class LinkedListHashtable(Hashtable):

    def __init__(self, size):
        self._size = size
        self._array = [None] * size
        self._md5 = hashlib.md5()

    def __setitem__(self, key, value):
        index = hash(key) % self._size
        if not self._array[index]:
            self._array[index] = LinkedList()
        linked_list = self._array[index]
        node = self._find(linked_list, key)
        if not node:
            self._array[index].insert((key, value))
        else:
            node.value = value

    def __getitem__(self, key: Any):
        linked_list = self._get_list(key)
        if not linked_list:
            return None
        node = self._find(linked_list, key)
        if not node:
            return None
        return node.value[1]

    def __contains__(self, key: Any) -> bool:
        linked_list = self._get_list(key)
        if not linked_list:
            return False
        return self._find(linked_list, key) is not None

    def __delitem__(self, key: Any) -> bool:
        linked_list = self._get_list(key)
        if not linked_list:
            return False
        index = self._find_index(linked_list, key)
        if index < 0:
            return False
        linked_list.delete(index)
        return True

    def get_keys(self):
        keys = []
        for i in range(self._size):
            linked_list = self._array[i]
            if not linked_list:
                continue
            keys.extend(self._collect_keys(linked_list))
        return keys

    def _get_list(self, key: Any) -> LinkedList:
        index = hash(key) % self._size
        return self._array[index]

    def _collect_keys(self, linked_list: LinkedList):
        keys = []
        current = linked_list.head
        while current:
            keys.append(current.value[0])
            current = current.next
        return keys

    @staticmethod
    def _find(linked_list: LinkedList, search_key: Any) -> LinkedList.LinkedListNode:
        current = linked_list.head
        while current:
            key, value = current.value
            if key == search_key:
                return current
            current = current.next
        return None

    @staticmethod
    def _find_index(linked_list: LinkedList, search_key: Any) -> int:
        current = linked_list.head
        index = 0
        while current:
            key, value = current.value
            if key == search_key:
                return index
            index += 1
            current = current.next
        return -1
