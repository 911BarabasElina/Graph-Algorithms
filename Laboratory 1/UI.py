from graph import create_random_graph, write_file
import unittest


def ui_create_graph():
    file_path_random_graph = "random_graph.txt"
    vertex = input("Give vertex: ")
    number_of_edges = input("Give number of vertices: ")

    if int(vertex) * int(vertex) < int(number_of_edges):
        print("The number of edges should be lest than number_of_vertices*number_of_vertices")
    else:
        create_random_graph(int(vertex), int(number_of_edges), file_path_random_graph)
        print("Successfully created!")


class UI(unittest.TestCase):

    def __init__(self, directed_graph):
        self.__graph = directed_graph

    def ui_number_of_vertices(self):

        number = self.__graph.get_number_of_vertices()
        print("The number of vertices is ", number)

    def ui_modify_cost(self):

        print("Do you want to get (1) or modify (2) the cost?\n ")
        option = input("1 or 2: ")
        origin = input(" Give the origin: ")
        target = input("\n Give the target: ")

        if not self.__graph.is_edge(int(origin), int(target)):
            print("There is no edge (", origin, ",", target, ")")
        else:
            if int(option) == 1:
                result = self.__graph.get_value_cost_dictionary(int(origin), int(target))
                for index in range(len(result)):
                    print("There cost of the edge: (", origin, ",", target, ") is:", str(result[index]))
            elif int(option) == 2:

                new_cost = input("Give the new cost: ")
                self.__graph.set_value_cost_dictionary(int(origin), int(target), int(new_cost))
                other_result = self.__graph.get_value_cost_dictionary(int(origin), int(target))
                print("The new cost of the edge: (", origin, ",", target, ") is:", str(other_result))

            else:
                print("Invalid option!\n")

    def ui_in_degree(self):

        vertex = input("Give vertex: ")
        if self.__graph.is_vertex(int(vertex)):
            print("The out degree of the vertex: ", vertex, " is: ", self.__graph.get_in_degree(int(vertex), 0))
            print("The in degree of the vertex: ", vertex, " is: ", self.__graph.get_out_degree(int(vertex), 0))
        else:
            print("The given vertex does not exist.")

    def ui_parse_vertices(self):

        # list_of_vertices = self.__graph.get_set_of_vertices()
        # vertices = iter(list_of_vertices)
        # while True:
        #     try:
        #         element = next(vertices)
        #         print(str(element))
        #     except StopIteration:
        #         break

        for index in self.__graph.parse_set_of_vertices():
            print(index)

            # if index > self.__graph.get_number_of_vertices():
            #   break

    def ui_parse_outbound_edges(self):

        vertex = input("Give vertex: ")

        if self.__graph.is_vertex(int(vertex)):
            print("The outbound edges of ", vertex, " are: ")
            ok = 0
            for index in self.__graph.get_outbound_edges(int(vertex)):
                ok = 1
                print("(", vertex, ",", index, ") ")
            if ok == 0:
                print("There are no outbound edges of ", vertex)
        else:
            print("The given vertex does not exist.")

    def ui_parse_inbound_edges(self):

        vertex = input("Give vertex: ")

        if self.__graph.is_vertex(int(vertex)):
            print("The inbound edges of ", vertex, " are: ")
            ok = 0
            for index in self.__graph.get_inbound_edges(int(vertex)):
                ok = 1
                print("(", index, ",", vertex, ") ")
            if ok == 0:
                print("There are no inbound edges of ", vertex)
        else:
            print("The given vertex does not exist.")

    def ui_add_edge(self):

        print(str(self.__graph.get_cost_dictionary()))
        print(str(self.__graph.get_predecessors_dictionary()))
        print(str(self.__graph.get_successors_dictionary()))

        origin = input(" Give the origin: ")
        target = input("\n Give the target: ")
        cost = input("\nGive the cost: ")

        if self.__graph.is_vertex(int(origin)) and self.__graph.is_vertex(int(target)):
            if not self.__graph.is_edge(int(origin), int(target)):
                self.__graph.add_edge(int(origin), int(target), int(cost))

                print(str(self.__graph.get_cost_dictionary()))
                print(str(self.__graph.get_predecessors_dictionary()))
                print(str(self.__graph.get_successors_dictionary()))
            else:
                print("This edge already exists")
        else:
            print("The given vertices does not exist.")

    def ui_remove_edge(self):

        print(str(self.__graph.get_cost_dictionary()))
        print(str(self.__graph.get_predecessors_dictionary()))
        print(str(self.__graph.get_successors_dictionary()))

        origin = input(" Give the origin: ")
        target = input("\n Give the target: ")
        if self.__graph.is_edge(int(origin), int(target)):
            self.__graph.remove_edge(int(origin), int(target))

            print(str(self.__graph.get_cost_dictionary()))
            print(str(self.__graph.get_predecessors_dictionary()))
            print(str(self.__graph.get_successors_dictionary()))
        else:
            print("There is no edge with this origin - target")

    def ui_is_edge(self):

        origin = input("Give origin: ")
        target = input("Give target: ")
        if self.__graph.is_edge(int(origin), int(target)):
            print("There is an edge from the first given vertex to the second one")
        else:
            print("There is no edge from the first given vertex to the second one")

    def ui_add_vertex(self):

        # vertex = input("Give the vertex: ")
        # if not self.__graph.is_vertex(int(vertex)):
        self.__graph.add_vertex()
        print("Vertex added successfully")

    # else:
    #     print("This vertex already exists")

    def ui_remove_vertex(self):
        vertex = input("Give the vertex: ")
        if not self.__graph.is_vertex(int(vertex)):
            print("This vertex does not exist")
        else:
            self.__graph.remove_vertex(int(vertex))

    def ui_parse_of_edges(self):

        print("The list of edges is: \n")
        for index in self.__graph.get_edges():
            print(str(index))

    def ui_copy_graph(self):

        new_graph = self.__graph.copy_graph()
        print("Successfully copied")
        return new_graph

    def test_functions(self):

        self.assertTrue(self.__graph.is_edge(0, 1))
        print(self.__graph.is_edge(0, 1))

        new_graph = self.__graph.copy_graph()

        self.assertTrue(new_graph.is_edge(0, 1))

        new_graph.remove_vertex(0)
        self.assertFalse(new_graph.is_edge(0, 1))
        print(new_graph.is_edge(0, 1))

        self.assertTrue(self.__graph.is_edge(0, 1))
        print(self.__graph.is_edge(0, 1))

        print("Passed!")

    def start(self):
        commands = {"0": self.test_functions, "1": self.ui_number_of_vertices, "2": self.ui_parse_vertices,
                    "3": self.ui_parse_of_edges,
                    "4": self.ui_in_degree, "5": self.ui_parse_outbound_edges, "6": self.ui_parse_inbound_edges,
                    "7": self.ui_modify_cost, "8": ui_create_graph, "9": self.ui_add_edge,
                    "10": self.ui_remove_edge, "11": self.ui_add_vertex, "12": self.ui_remove_vertex,
                    "13": self.ui_is_edge, "14": self.ui_copy_graph}

        while True:

            write_file("graphs.txt", self.__graph)

            print("\n 0. Test setup!\n"
                  " 1. Print the number of vertices\n"
                  " 2. Parse the set of vertices\n"
                  " 3. Parse the list of edges\n"
                  " 4. The in/out degree of a given vertex\n"
                  " 5. Parse the set of outbound edges\n"
                  " 6. Parse the set of inbound edges\n"
                  " 7. Retrieve or modify the information attached to a specified edge.\n"
                  " 8. Create random graph\n"
                  " 9. Add an edge\n"
                  "10. Remove an edge\n"
                  "11. Add a vertex\n"
                  "12. Remove a vertex\n"
                  "13. Check the existence of an edge\n"
                  "14. Copy graph\n"
                  "15. Exit!\n")

            command = input("Give command > ")
            if command in commands:
                commands[command]()
            elif command == "15":
                break
            else:
                print("Invalid choice.")
