from trees import BinarySearchTree


def test_binary_search_tree():

    tree = BinarySearchTree()
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(4)
    tree.insert(8)
    #TODO: tree.traverse(lambda x: print(x))

    assert 4 in tree
    assert 9 not in tree

    assert tree.min() == 1
    assert tree.max() == 8

