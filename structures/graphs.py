from abc import ABC
from typing import Callable, Any
from structures.lists import Queue


class Edge:

    def __init__(self, source, target, weight=None):
        self.weight = weight
        self.source = source
        self.target = target

    def __repr__(self):
        return f"({self.source}, {self.target})"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.source == other.source and self.target == other.target

    def __hash__(self):
        return hash((self.source, self.target))


class Graph(ABC):

    def __contains__(self, vertex):
        pass

    def __iter__(self):
        pass

    def get_adjacent_edges(self, vertex):
        pass

    def get_adjacent_vertices(self, vertex):
        pass


class MutableAdjacencyGraph(Graph):

    def __init__(self, directed=True):
        self.degree = 0
        self.num_vertices = 0
        self.num_edges = 0
        self.directed = directed
        self.adjacency = {}

    def __contains__(self, vertex):
        return vertex in self.adjacency

    def __iter__(self):
        for vertex in self.adjacency.keys():
            yield vertex

    def get_adjacent_edges(self, vertex):
        return self.adjacency[vertex]

    def get_adjacent_vertices(self, vertex):
        return [edge.target for edge in self.adjacency[vertex]]

    def add_vertex(self, label):
        if label not in self.adjacency:
            self.adjacency[label] = []
            self.num_vertices += 1

    def add_edge(self, source, target, weight=None):
        self.add_vertex(source)
        self.add_vertex(target)
        # check if edge exists
        edge = Edge(source, target, weight)
        if edge in self.adjacency[source]:
            return
        self.adjacency[source].append(edge)
        if not self.directed:
            reverse_edge = Edge(target, source, weight)
            if reverse_edge not in self.adjacency[target]:
                self.adjacency[target].append(reverse_edge)
        self.num_edges += 1

    @staticmethod
    def read_graph(filename, directed=True):
        graph = MutableAdjacencyGraph(directed=directed)
        with open(filename) as file:
            for line in file:
                tokens = line.strip().split(':')
                source = tokens[0].strip()
                targets = tokens[1].split()
                for target in targets:
                    graph.add_edge(source, target.strip())
        return graph


def traverse_dfs(graph: Graph, visitor: Callable[[Any], None]):
    def _traverse(graph: Graph, vertex, visitor, visited):
        if vertex in visited:
            return
        visitor(vertex)
        visited.add(vertex)
        for neighbor in graph.get_adjacent_vertices(vertex):
            _traverse(graph, neighbor, visitor, visited)

    visited = set()
    for vertex in graph:
        _traverse(graph, vertex, visitor, visited)


def traverse_bfs(graph: Graph,
                 vertex_visitor: Callable[[Any], None] = lambda v: None,
                 edge_visitor: Callable[[Any], None] = lambda e: None):
    queue = Queue()
    visited = set()
    for vertex in graph:
        queue.add(vertex)
        while len(queue) > 0:
            v = queue.remove()
            if v in visited:
                continue
            visited.add(v)
            vertex_visitor(v)
            for edge in graph.get_adjacent_edges(v):
                edge_visitor(edge)
                neighbor = edge.target
                if neighbor not in visited:
                    queue.add(neighbor)
