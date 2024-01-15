from structures.hashtable import *


def test_linked_list_hashtable():
    hashtable = LinkedListHashtable(10)
    hashtable['James'] = 'Peach'
    hashtable['Mario'] = 'Brother'
    hashtable['Laurel'] = 'Hardy'
    keys = hashtable.get_keys()
    assert len(keys) == 3
    for key in keys:
        assert key in hashtable

    assert hashtable['Mario'] == 'Brother'
    # make sure we have collisions
    for i in range(20):
        hashtable[i] = i
    keys = hashtable.get_keys()
    assert len(keys) == 23

    del hashtable[10]
    assert len(hashtable.get_keys()) == 22


def test_chained_hashtable():
    hashtable = ChainedHashtable(10)
    hashtable['James'] = 'Peach'
    hashtable['Mario'] = 'Brother'
    hashtable['Laurel'] = 'Hardy'
    keys = hashtable.get_keys()
    assert len(keys) == 3
    for key in keys:
        assert key in hashtable
    assert hashtable['Mario'] == 'Brother'
    #print(hashtable)


