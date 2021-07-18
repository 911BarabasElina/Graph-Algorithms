import random
import copy


class DirectedGraph:

    def __init__(self, n, m):
        self._n = n
        self._m = m
        self._vertices_list = []
        self._successors_dictionary = {}
        self._predecessors_dictionary = {}
        self._cost_dictionary = {}
        self.initial_keys()
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

    def get_successors_dictionary(self):
        return self._successors_dictionary

    def get_predecessors_dictionary(self):
        return self._predecessors_dictionary

    def get_cost_dictionary(self):
        return self._cost_dictionary

    def get_in_degree(self, vertex, remove):
        return len(self._successors_dictionary[vertex]) - remove

    def get_out_degree(self, vertex, remove):
        return len(self._predecessors_dictionary[vertex]) - remove

    def get_outbound_edges(self, vertex):

        list_of_predecessors = self._predecessors_dictionary[vertex]

        for value in list_of_predecessors:
            yield value

    def get_inbound_edges(self, vertex):

        list_of_successors = self._successors_dictionary[vertex]

        for value in list_of_successors:
            yield value

    def get_cost(self, key):
        return self._cost_dictionary[key]

    def set_value_cost_dictionary(self, origin, target, new_value):
        key = (origin, target)
        self._cost_dictionary[key] = new_value

    def set_keys(self, key, values, in_out):

        if in_out == "inbound":
            self._successors_dictionary.setdefault(key, []).append(values)
        elif in_out == "outbound":
            self._predecessors_dictionary.setdefault(key, []).append(values)
        else:
            # self.__cost_dictionary.setdefault(key,[]).append(values)
            self._cost_dictionary[key] = values

    def add_vertex(self):
        # self.__vertices.append(vertex)
        # self.__predecessors_dictionary[vertex] = []
        # self.__successors_dictionary[vertex] = []
        # self.__n = self.__n + 1
        self._vertices_list.append(self._n)
        self._predecessors_dictionary[self._n] = []
        self._successors_dictionary[self._n] = []
        self._n = self._n + 1

    def remove_vertex(self, vertex):
        self._vertices_list.remove(vertex)
        self._predecessors_dictionary.pop(vertex)
        self._successors_dictionary.pop(vertex)

        for index in self._vertices_list:
            if self.is_edge(index, vertex):
                pair = (index, vertex)
                self._cost_dictionary.pop(pair)
                self._m = self._m - 1

            if self.is_edge(vertex, index):
                pair = (vertex, index)
                self._cost_dictionary.pop(pair)
                self._m = self._m - 1

        self._n = self._n - 1

    def add_edge(self, origin, target, cost):

        cost_list = [cost]
        key = (origin, target)
        self._cost_dictionary[key] = cost_list
        self.set_keys(target, origin, "outbound")
        self.set_keys(origin, target, "inbound")
        self._m = self._m + 1

    def remove_edge(self, origin, target):

        key = (origin, target)
        self._cost_dictionary.pop(key)
        list_of_predecessors = self._predecessors_dictionary[target]
        list_of_predecessors.remove(origin)

        list_of_successors = self._successors_dictionary[origin]
        list_of_successors.remove(target)
        self._m = self._m - 1

    def initial_keys(self):

        for key in range(self._n):
            self._successors_dictionary[key] = list()
            self._predecessors_dictionary[key] = list()

    def initial_vertices(self):
        for index in range(self._n):
            self._vertices_list.append(index)

    def parse_set_of_vertices(self):
        for vertex in self._vertices_list:
            yield vertex

    def is_edge(self, origin, target):
        edge = (origin, target)
        return edge in self._cost_dictionary.keys()

    def is_vertex(self, vertex):
        return vertex in self._predecessors_dictionary.keys()

    def copy_graph(self):
        return copy.deepcopy(self)


def write_file(file_path, graph):
    file = open(file_path, "w")

    file.writelines([str(graph.get_number_of_vertices()), " ", str(graph.get_number_of_edges()), "\n"])
    for index in graph.get_edges():
        origin = index[0]
        target = index[1]
        cost = graph.get_cost(index)
        # cost = graph.get_cost(index)
        file.writelines([str(origin), " ", str(target), " ", str(cost), "\n"])

    file.close()


def read_file(file_path):
    file = open(file_path, "r")
    n, m = map(int, file.readline().split())
    one_graph = DirectedGraph(int(n), int(m))

    for edge in range(m):
        origin, target, cost = map(int, file.readline().split())
        if cost is not None:
            key_pair = (int(origin), int(target))
            one_graph.set_keys(key_pair, int(cost), "cost")
            # one_graph.set_keys(target, origin, "inbound")
            # one_graph.set_keys(origin, target, "outbound")
            one_graph.set_keys(int(target), int(origin), "outbound")
            one_graph.set_keys(int(origin), int(target), "inbound")

    file.close()
    return one_graph


def create_random_graph(vertex, number_of_edges, file_path):
    file = open(file_path, "w")
    file.writelines([str(vertex), " ", str(number_of_edges), "\n"])

    for index in range(int(number_of_edges)):
        origin = random.randint(0, int(vertex) - 1)
        target = random.randint(0, int(vertex) - 1)
        cost = random.randint(0, 10)
        file.writelines([str(origin), " ", str(target), " ", str(cost), "\n"])

    file.close()
