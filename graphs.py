# Basic Graph Implementation
from fontTools.ttLib.tables.otTraverse import dfs_base_table

vertx_data = ["A", "B", "C", "D"]
print(vertx_data.index("A"))

adjacency_matrix = [
    [0, 1, 1, 1],  # Edges for A
    [1, 0, 1, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D
]

def print_adjacency_matrix(matrix):
    print("\nAdjacency Matrix:")
    for row in matrix:
        for i in row:
            print(" ", i, end="")
        print()

print("vertex_data: ", vertx_data)
print_adjacency_matrix(adjacency_matrix)


def print_connections(matrix, vertices):
    print("\nConnections for each vertex:")
    for i in range(len(vertices)):
        print(f"{vertices[i]} ", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:  # if there is a connection
                print("-", vertices[j], end=" ")
        print()

print_connections(adjacency_matrix, vertx_data)



# Graph implementation using classes, undirected and no weighted
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for i in self.vertex_data:
            print(i, end=" ")
        print()
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

    def dfs(self, start_vertex_data):    # the argument is the first vertex where to start
        visited = [False] * self.size    # a new list fill with False, then add the traversed vertices
        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)

    def dfs_util(self, v, visited):  # v is the start vertx index and visited is the list that add after traversing
        visited[v] = True
        print(self.vertex_data[v], end=" ")

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)


    def bsf(self, start_vertex_data):
        queue = [self.vertex_data.index(start_vertex_data)]
        visited = [False] * self.size



g = Graph(4)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1)  # A - B
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(1, 2)  # B - C

g.print_graph()
print()
print()
# graph implementation using class, directed and weighted

class GraphDirectedAndWeighted:
    def __init__(self, size):
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [""] * size

    def add_edge(self, u, v, weight):
        if self.size > u >= 0 and self.size > v >= 0:
            self.adj_matrix[u][v] = weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")





h = GraphDirectedAndWeighted(4)
h.add_vertex_data(0, 'A')
h.add_vertex_data(1, 'B')
h.add_vertex_data(2, 'C')
h.add_vertex_data(3, 'D')
h.add_edge(0, 1, 3)  # A -> B with weight 3
h.add_edge(0, 2, 2)  # A -> C with weight 2
h.add_edge(3, 0, 4)  # D -> A with weight 4
h.add_edge(2, 1, 1)  # C -> B with weight 1

h.print_graph()
































