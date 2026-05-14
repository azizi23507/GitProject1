# Basic Graph Implementation


vertx_data = ["A", "B", "C", "D"]
adjacency_matrix = [
    [0, 1, 1, 1],  # Edges for A
    [1, 0, 1, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D
]

def print_adjacency_matrix(matrix):
    print("\nAdjacency Matrix:")
    print("  ", end="")
    for i in vertx_data:
        print(i, end=" ")
    print()
    index = 0
    for row in matrix:
        print(*vertx_data[index], end="")
        for i in row:
            print("", i, end="")
        index += 1
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
print()
print()


# Graph implementation using class, undirected and unweighted
print("Graph implementation using class, undirected and unweighted")
print()
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


    def bfs(self, start_vertex_data):
        queue = [self.vertex_data.index(start_vertex_data)] # index of the vertex argument
        visited = [False] * self.size
        visited[queue[0]] = True

        while queue:
            current_vertex = queue.pop(0)
            print(self.vertex_data[current_vertex], end=" ")

            for i in range(self.size):
                if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def dfs_util_cycle(self, v, visited, parent):
        visited[v] = True

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1:
                if not visited[i]:
                    if self.dfs_util_cycle(i, visited, v):
                        return True
                elif parent != i:
                    return True
        return False

    def is_cyclic(self):
        visited = [False] * self.size
        for i in range(self.size):
            if not visited[i]:
                if self.dfs_util_cycle(i, visited, -1):
                    return True
        return False



g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.print_graph()
print()
print()
print("\nDepth First Search starting from vertex D:")
g.dfs('D')
print()
print("\nBreadth First Search starting from vertex D:")
g.bfs('D')
print()
g.print_graph()
print("\nGraph has cycle:", g.is_cyclic())

print()
print()


# graph implementation using class, directed and weighted
print("graph implementation using class directed and weighted")
print()
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

    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=' ')

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex_data):
        visited = [False] * self.size

        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)

    def bfs(self, start_vertex_data):
        queue = [self.vertex_data.index(start_vertex_data)]
        visited = [False] * self.size
        visited[queue[0]] = True

        while queue:
            current_vertex = queue.pop(0)
            print(self.vertex_data[current_vertex], end=' ')

            for i in range(self.size):
                if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def dfs_util_cycle(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True
        print("Current vertex:", self.vertex_data[v])

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1:
                if not visited[i]:
                    if self.dfs_util_cycle(i, visited, rec_stack):
                        return True
                elif rec_stack[i]:
                    return True

        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.size
        rec_stack = [False] * self.size
        for i in range(self.size):
            if not visited[i]:
                print()  # new line
                if self.dfs_util_cycle(i, visited, rec_stack):
                    return True
        return False


h = GraphDirectedAndWeighted(7)

h.add_vertex_data(0, 'A')
h.add_vertex_data(1, 'B')
h.add_vertex_data(2, 'C')
h.add_vertex_data(3, 'D')
h.add_vertex_data(4, 'E')
h.add_vertex_data(5, 'F')
h.add_vertex_data(6, 'G')

h.add_edge(3, 0, 1)  # D -> A
h.add_edge(3, 4, 1)  # D -> E
h.add_edge(4, 0, 1)  # E -> A
h.add_edge(0, 2, 1)  # A -> C
h.add_edge(2, 5, 1)  # C -> F
h.add_edge(2, 6, 1)  # C -> G
h.add_edge(5, 1, 1)  # F -> B
h.add_edge(1, 2, 1)  # B -> C

h.print_graph()

print("\nDepth First Search starting from vertex D:")
h.dfs('D')

print("\n\nBreadth First Search starting from vertex D:")
h.bfs('D')

print("\nGraph has cycle:", h.is_cyclic())


































