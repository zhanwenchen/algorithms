from lexicographic_bfs import lex_bfs


graph_dict = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'c', 'd'],
    'c': ['a', 'b', 'd', 'g', 'f'],
    'd': ['a', 'b', 'c', 'e', 'g'],
    'e': ['d'],
    'f': ['c', 'g'],
    'g': ['c', 'd', 'f'],
}

# initial_ordering = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
initial_ordering = ['f', 'g', 'c', 'd', 'b', 'a', 'e']


if __name__ == '__main__':
    print(lex_bfs(graph_dict, initial_ordering))
