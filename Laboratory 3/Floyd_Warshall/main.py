import copy
import math
import random


class DirectedGraph:

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
        return int(self._cost_dictionary[key])

    def set_value_cost_dictionary(self, origin, target, new_value):
        key = (origin, target)
        self._cost_dictionary[key] = int(new_value)

    def set_keys(self, key, values):
        self._cost_dictionary[key] = values

    def add_vertex(self):

        self._vertices_list.append(self._n)
        self._n = self._n + 1

    def add_edge(self, origin, target, cost):

        cost_list = [cost]
        key = (origin, target)
        self._cost_dictionary[key] = cost_list
        self._m = self._m + 1

    def initial_vertices(self):
        for index in range(1, self._n + 1):
            self._vertices_list.append(index)

    def parse_set_of_vertices(self):
        for vertex in self._vertices_list:
            yield vertex

    def copy_graph(self):
        return copy.deepcopy(self)

    def is_edge(self, origin, target):
        edge = (origin, target)
        return edge in self._cost_dictionary.keys()


def read_file(file_path):
    file = open(file_path, "r")
    n, m = map(int, file.readline().split())
    one_graph = DirectedGraph(int(n), int(m))

    for edge in range(m):
        origin, target, cost = map(int, file.readline().split())
        if cost is not None:
            key_pair = (int(origin), int(target))
            one_graph.set_keys(key_pair, int(cost))

    file.close()
    return one_graph


def create_random_graph(vertex, number_of_edges, file_path):
    file = open(file_path, "w")
    file.writelines([str(vertex), " ", str(number_of_edges), "\n"])

    for index in range(int(number_of_edges)):
        origin = random.randint(1, int(vertex))
        target = random.randint(1, int(vertex))
        cost = random.randint(1, 10)
        file.writelines([str(origin), " ", str(target), " ", str(cost), "\n"])

    file.close()


def Floyd_Warshall_Algorithm(graph, source, destination):
    distances_dictionary = {}
    next_vertex_dictionary = {}

    for i in graph.get_set_of_vertices():
        for j in graph.get_set_of_vertices():
            if graph.is_edge(i, j):
                distances_dictionary[(i, j)] = graph.get_cost((i, j))
                next_vertex_dictionary[(i, j)] = j
            else:
                distances_dictionary[(i, j)] = math.inf
                next_vertex_dictionary[(i, j)] = -1
        distances_dictionary[(i, i)] = 0
        next_vertex_dictionary[(i, i)] = i

    for k in graph.get_set_of_vertices():
        for i in graph.get_set_of_vertices():
            for j in graph.get_set_of_vertices():
                if distances_dictionary[(i, k)] + distances_dictionary[(k, j)] < distances_dictionary[(i, j)]:
                    distances_dictionary[(i, j)] = distances_dictionary[(i, k)] + distances_dictionary[(k, j)]
                    next_vertex_dictionary[(i, j)] = next_vertex_dictionary[(i, k)]

    print("\n")

    if next_vertex_dictionary[(source, destination)] == -1:
        return None
    else:
        path = [source]
        current_node = source
        while current_node != destination:
            path.append(next_vertex_dictionary[(current_node, destination)])
            current_node = next_vertex_dictionary[(current_node, destination)]

        for i in graph.get_set_of_vertices():
            line = ""
            for j in graph.get_set_of_vertices():
                line += str(distances_dictionary[(i, j)]).center(5) + " "
            print(line)

        print("\n")
        print("From the source:", source, "to the destination:", destination, "the path is:", path,
              "and the cost of the walk is:", distances_dictionary[(source, destination)])
        print("\n")


if __name__ == "__main__":

    #create_random_graph(10, 56, "random_graph.txt")
    graph_from_file = read_file("floyd_warshall_graph.txt")

    print("\nFloyd-Warshall Algorithm\n")
    print("The vertices are from 1 to", graph_from_file.get_number_of_vertices())

    while True:

        source = input("Source: ")
        destination = input("Destination: ")

        Floyd_Warshall_Algorithm(graph_from_file, int(source), int(destination))

        option = input("Do you want to continue? y/n ")
        if option == "n":
            break
