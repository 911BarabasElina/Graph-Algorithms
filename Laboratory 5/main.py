import random


# 4. Given an undirected graph, find a Hamiltonian cycle (if it exists).

class UndirectedGraph:

    def __init__(self, n, m):
        self._n = n
        self._m = m
        self._vertices_list = []
        self._cost_dictionary = {}
        self.initial_vertices()

    def get_number_of_vertices(self):
        return self._n

    def get_number_of_edges(self):
        return self._m

    def get_value_cost_dictionary(self, origin, target):
        key = (origin, target)
        return self._cost_dictionary[key]

    def get_edges(self):

        for key, value in self._cost_dictionary.items():
            yield key

    def get_set_of_vertices(self):
        return self._vertices_list

    def get_cost_dictionary(self):
        return self._cost_dictionary

    def get_cost(self, key):
        return self._cost_dictionary[key]

    def set_keys(self, key, values):

        self._cost_dictionary[key] = values

    def initial_vertices(self):
        for index in range(self._n + 1):
            self._vertices_list.append(index)

    def is_edge(self, origin, target):
        edge = (origin, target)
        return edge in self._cost_dictionary.keys()

    def adjacent_vertices(self, vertex, nr_elements_path, path):

        if self.is_edge(vertex, path[nr_elements_path - 1]) is False:
            return False

        for one_vertex in path:
            if one_vertex == vertex:
                return False

        return True

    def is_hamiltonian_cycle_backtracking(self, path, nr_elements_path):

        if nr_elements_path == self._n:
             if self.is_edge(path[0], path[nr_elements_path - 1]):
                    return True
        #return False

        for vertex in range(1, self._n):
            if self.adjacent_vertices(vertex, nr_elements_path, path):
                path[nr_elements_path] = vertex
                if self.is_hamiltonian_cycle_backtracking(path, nr_elements_path + 1):
                    return True
                path[nr_elements_path] = -1

        return False

    def hamiltonian_cycle(self):

        path = [-1] * self._n
        path[0] = 0

        if not self.is_hamiltonian_cycle_backtracking(path, 1):
            print("There is no Hamiltonian cycle in the given graph")
            return False
        self.print_solution(path)
        return True

    def print_solution(self, path):

        print("\n")

        for vertex in path:
            print(vertex, end=" ")
        print(path[0],end=" -> ")

        print("is a Hamiltonian cycle from the given graph")


def read_file(file_path):
    file = open(file_path, "r")
    n, m = map(int, file.readline().split())
    one_graph = UndirectedGraph(int(n), int(m))

    for edge in range(m):
        origin, target, cost = map(int, file.readline().split())
        if cost is not None:
            key_pair = (int(origin), int(target))
            one_graph.set_keys(key_pair, int(cost))
            key_pair_2 = (int(target), int(origin))
            one_graph.set_keys(key_pair_2, int(cost))

    file.close()
    return one_graph


g = read_file("graph.txt")
g.hamiltonian_cycle()
