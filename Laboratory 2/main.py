def read_file(file_path, one_graph):
    file = open(file_path, "r")
    n, m = map(int, file.readline().split())
    for edge in range(m):
        one_vertex, second_vertex = map(int, file.readline().split())
        one_graph.add_edge(one_vertex, second_vertex)
        one_graph.add_edge(second_vertex, one_vertex)

    file.close()


class UndirectedGraph:

    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.dictionary = {}
        for i in range(number_of_vertices):
            self.dictionary[i] = []

    def add_edge(self, one_vertex, second_vertex):
        self.dictionary[one_vertex].append(second_vertex)

    def DepthFirstSearch(self, current_connected_component, vertex, visited):

        visited[vertex] = True
        current_connected_component.append(vertex)
        for i in self.dictionary[vertex]:
            if not visited[i]:
                current_connected_component = self.DepthFirstSearch(current_connected_component, i, visited)
        return current_connected_component

    def connectedComponents(self):

        visited = []
        connected_components = []
        for i in range(self.number_of_vertices):
            visited.append(False)
        for vertex in range(self.number_of_vertices):
            if not visited[vertex]:
                current_connected_component = []
                connected_components.append(self.DepthFirstSearch(current_connected_component, vertex, visited))
        return connected_components


def run():
    file_path = "graphs.txt"
    file = open(file_path, "r")
    n, m = map(int, file.readline().split())
    undirected_graph = UndirectedGraph(n)
    read_file("graphs.txt", undirected_graph)

    connected_components = undirected_graph.connectedComponents()
    for element in connected_components:
        print(str(element) + " is a connected component")


run()
