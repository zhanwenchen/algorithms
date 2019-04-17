'''
pytest only. There's no main method.
'''

from lexicographic_bfs import lex_bfs


##########
# Test 1 #
##########
graph_dict_1 = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'c', 'd'],
    'c': ['a', 'b', 'd', 'g', 'f'],
    'd': ['a', 'b', 'c', 'e', 'g'],
    'e': ['d'],
    'f': ['c', 'g'],
    'g': ['c', 'd', 'f'],
}

initial_ordering_1 = ['f', 'g', 'c', 'd', 'b', 'a', 'e']

def test_lex_bfs_1():
    assert lex_bfs(graph_dict_1, initial_ordering_1) == {
        'f': 0,
        'g': 1,
        'c': 2,
        'd': 3,
        'b': 4,
        'a': 5,
        'e': 6,
    }


##########
# Test 2 #
##########
graph_dict_2 = {
    'a': ['y', 'u', 'v', 'w', 'z'],
    'b': ['d', 'y', 'u', 'v', 'w'],
    'c': ['d', 'y', 'u', 'v', 'w'],
    'd': ['y', 'u', 'v', 'w', 'c', 'b'],
    'e': ['y', 'u', 'v', 'w'],
    'u': ['x', 'd', 'e', 'v', 'c', 'a', 'z', 'b'],
    'v': ['x', 'd', 'u', 'e', 'c', 'a', 'z', 'b'],
    'w': ['x', 'd', 'y', 'e', 'c', 'a', 'z', 'b'],
    'x': ['y', 'u', 'v', 'w', 'z'],
    'y': ['x', 'w', 'z', 'd', 'e', 'c', 'a', 'b'],
    'z': ['x', 'y', 'w', 'u', 'v', 'a'],
}

initial_ordering_2 = ['x', 'd', 'y', 'u', 'e', 'v', 'w', 'c', 'a', 'z', 'b']

def test_lex_bfs_2():
    assert lex_bfs(graph_dict_2, initial_ordering_2) == {
        'x': 0,
        'y': 1,
        'w': 2,
        'z': 3,
        'u': 4,
        'v': 5,
        'a': 6,
        'd': 7,
        'c': 8,
        'b': 9,
        'e': 10,
    }


def main():
    pass


if __name__ == '__main__':
    main()
