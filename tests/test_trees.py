from structures.trees import BinarySearchTree, TraverseOrder


def test_binary_search_tree():

    tree = BinarySearchTree()
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(4)
    tree.insert(8)
    assert len(tree) == 5

    values = []
    tree.traverse(lambda x: values.append(x))
    assert values == [2, 1, 7, 4, 8]
    values = []
    tree.traverse(lambda x: values.append(x), traverse_order=TraverseOrder.IN_ORDER)
    assert values == [1, 2, 4, 7, 8]
    values = []
    tree.traverse(lambda x: values.append(x), traverse_order=TraverseOrder.POST_ORDER)
    assert values == [1, 4, 8, 7, 2]

    assert 4 in tree
    assert 9 not in tree

    assert tree.min() == 1
    assert tree.max() == 8

