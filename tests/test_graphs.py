from structures.graphs import *
import os

# Set the working directory to the parent directory
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_read():
    graph = MutableAdjacencyGraph.read_graph("tinyFile.txt")
    assert graph.num_vertices == 8
    assert graph.num_edges == 13
    assert 'G' in graph
    assert 'U' not in graph
    assert str(graph.get_adjacent_edges('F')) == '[(F, E), (F, B)]'
    assert str(graph.get_adjacent_edges('H')) == '[]'
    assert str(graph.get_adjacent_vertices('C')) == "['G', 'F', 'H']"


def test_dfs():
    graph = MutableAdjacencyGraph.read_graph("tinyFile.txt")
    vertices = []
    traverse_dfs(graph, lambda v: vertices.append(v))
    assert vertices == ['A', 'F', 'E', 'B', 'C', 'G', 'H', 'D']


def test_bfs():
    graph = MutableAdjacencyGraph.read_graph("tinyFile.txt")
    vertices = []
    traverse_bfs(graph, lambda v: vertices.append(v))
    assert vertices == ['A', 'F', 'B', 'C', 'H', 'G', 'E', 'D']

