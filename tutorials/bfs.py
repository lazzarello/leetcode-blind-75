# https://stackabuse.com/graphs-in-python-breadth-first-search-bfs-algorithm/
# This one is not a scam. It's a very good example and tutorial. Thanks!
# this is a data structure for a queue that's built into Python
from queue import Queue

class Graph:
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        self.m_directed = directed

        # this website calls it "an adjacency matrix"
        self.m_adj_list = {node: set() for node in self.m_nodes}

    # Add edge to graph
    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))

    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])

    def bfs(self, start_node, target_node):

        visited = set()
        queue = Queue()

        queue.put(start_node)
        visited.add(start_node)

        parent = dict()
        parent[start_node] = None

        path_found = False
        while not queue.empty():
            current_node = queue.get()
            if current_node == target_node:
                path_found = True
                break

            for (next_node, weight) in self.m_adj_list[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    parent[next_node] = current_node
                    visited.add(next_node)

        path = []
        if path_found:
            path.append(target_node)
            while parent[target_node] is not None:
                path.append(parent[target_node])
                target_node = parent[target_node]
            path.reverse()
        return path

graph = Graph(6, directed=False)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 5)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 5)

graph.print_adj_list()
for end in range(6):
    path = []
    path = graph.bfs(4,end)
    print(path)
