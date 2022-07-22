class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} : {self.adj_list[vertex]}")

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.adj_list.keys() and vertex_2 in self.adj_list.keys():
            self.adj_list[vertex_2].append(vertex_1)
            self.adj_list[vertex_1].append(vertex_2)
            return True
        return False
