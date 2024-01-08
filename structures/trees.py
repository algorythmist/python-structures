from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import Any, TypeVar, Callable


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass


C = TypeVar('C', bound=Comparable)


class TraverseOrder(Enum):
    PRE_ORDER = 1
    IN_ORDER = 2
    POST_ORDER = 3


class BinarySearchTree:
    class BinaryTreeNode:

        def __init__(self, value: C):
            self._value = value
            self._left = None
            self._right = None
            self._parent = None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, value):
        return self._find(value, self._root) is not None

    def _find(self, value: C, node: BinaryTreeNode) -> BinaryTreeNode:
        if not node:
            return None
        if value == node._value:
            return node
        if value < node._value:
            return self._find(value, node._left)
        else:
            return self._find(value, node._right)

    def insert(self, value: C):
        self._root = self._insert(value, self._root, None)
        self._size += 1

    def _insert(self, value: C, node: BinaryTreeNode, parent: BinaryTreeNode) -> BinaryTreeNode:
        if not node:
            node = BinarySearchTree.BinaryTreeNode(value)
            node._parent = parent
            return node
        if value < node._value:
            node._left = self._insert(value, node._left, node)
        else:
            node._right = self._insert(value, node._right, node)
        return node

    def traverse(self, visitor: Callable[[C], None], traverse_order: TraverseOrder = TraverseOrder.PRE_ORDER):
        self._traverse(visitor, self._root, traverse_order)

    def _traverse(self, visitor: Callable[[C], None], node: BinaryTreeNode, traverse_order: TraverseOrder):
        if not node:
            return
        if traverse_order == TraverseOrder.PRE_ORDER:
            visitor(node._value)
        self._traverse(visitor, node._left, traverse_order)
        if traverse_order == TraverseOrder.IN_ORDER:
            visitor(node._value)
        self._traverse(visitor, node._right, traverse_order)
        if traverse_order == TraverseOrder.POST_ORDER:
            visitor(node._value)

    def min(self) -> C:
        if not self._root:
            return None
        return self._min(self._root._left)

    def _min(self, node: BinaryTreeNode) -> C:
        if not node._left:
            return node._value
        return self._min(node._left)

    def max(self) -> C:
        if not self._root:
            return None
        return self._max(self._root._right)

    def _max(self, node: BinaryTreeNode) -> C:
        if not node._right:
            return node._value
        return self._max(node._right)