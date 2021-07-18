import random


# Write a program that, given an undirected connected graph, constructs
# a minumal spanning tree using the Kruskal's algorithm.

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

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root

        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def KruskalMST(self):

        result = []
        i = 0
        number_of_required_edges = 0

        sorted_copy_keys = sorted(self._cost_dictionary,
                                  key=self._cost_dictionary.get)

        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #print(str(sorted_copy_keys))
        print("Initial: ", self.get_cost_dictionary())
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        sorted_copy_values = sorted(self._cost_dictionary.values())
        #print(str(sorted_copy_values))
        #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


        sorted_dictionary = dict(zip(sorted_copy_keys, sorted_copy_values))

        self._cost_dictionary = sorted_dictionary

        print("Sorted: ",self.get_cost_dictionary())
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        parent = []
        rank = []

        for node in range(self._n):
            parent.append(node)
            rank.append(0)

        while number_of_required_edges < self._n - 1:

            u, v = sorted_copy_keys[i]
            w = sorted_copy_values[i]

            i = i + 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                number_of_required_edges = number_of_required_edges + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)


def read_file(file_path):
    file = open(file_path, "r")
    n, m = map(int, file.readline().split())
    one_graph = UndirectedGraph(int(n), int(m))

    for edge in range(m):
        origin, target, cost = map(int, file.readline().split())
        if cost is not None:
            key_pair = (int(origin), int(target))
            one_graph.set_keys(key_pair, int(cost))

    file.close()
    return one_graph


g = read_file("graph.txt")


g.KruskalMST()
