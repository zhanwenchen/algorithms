'''
Lexicographic Breadth-First Search (Lex-BFS)
'''
def lex_bfs(graph, initial_ordering):
    '''
    Args:
        :param graph: dicitonary of flat lists.
        :param initial_ordering: list.
    '''
    final_ordering = {}
    partitions_list = [initial_ordering]
    final_ordering_position = 0
    print('init: partitions_list =', partitions_list)
    while partitions_list and partitions_list[0]:
        print('\tStarting partitions_list =', partitions_list)
        first_partition = partitions_list[0]
        # print('\tfirst_partition =', first_partition)
        try:
            pivot_vertex = first_partition.pop(0) # pivot_vertex = partitions_list[0] # NOTE that partition_list[0] can become [] if it only had a single element
        except IndexError as e:
            print('\tIndexError: first_partition =', first_partition)
            raise
        final_ordering[pivot_vertex] = final_ordering_position
        final_ordering_position += 1
        pivot_neigbors = get_neighbors(graph, pivot_vertex)
        print('\tpivot_vertex = {}, pivot_neigbors = {}'.format(pivot_vertex, pivot_neigbors))
        new_partitions_list = []
        for partition in partitions_list:
            if not partition:
                continue
            # pivot_neighbors_in_partition = set(partition).intersection(pivot_neigbors)
            pivot_neighbors_in_partition = [el for el in partition if el in pivot_neigbors]
            print('\t\tpartition {}: the neighbors of {} in it are {}'.format(partition, pivot_vertex, pivot_neighbors_in_partition))
            if not pivot_neighbors_in_partition:
                print('\t\tAppending original partition={}: pivot_neighbors_in_partition {} is empty'.format(partition, pivot_neighbors_in_partition))
                new_partitions_list.append(partition)
                continue

            if set(pivot_neighbors_in_partition) == set(partition):
                print('\t\tAppending original partition={}: pivot_neighbors_in_partition == partition'.format(partition))
                new_partitions_list.append(partition)
                continue

            # partition = list(set(partition) - pivot_neighbors_in_partition)
            partition = [el for el in partition if el not in pivot_neighbors_in_partition]
            new_partitions_list.extend([pivot_neighbors_in_partition, partition])
            print('\t\tAppending pivot_neighbors_in_partition={}: and partition={}. new_partitions_list is now {}'.format(pivot_neighbors_in_partition, partition, new_partitions_list))

        partitions_list = new_partitions_list
        print('\tEnding partitions_list =', partitions_list)

    return final_ordering


def get_neighbors(graph, vertex):
    return graph[vertex]
