from unittest import TestCase
from DiGraph import DiGraph
from Node import Node


# graph creator of 10 nodes 12 edges.
def graph_creator():
    g = DiGraph()
    for i in range(10):
        g.add_node(i)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 8, 2)
    g.add_edge(9, 0, 1)
    g.add_edge(1, 5, 2.5)
    g.add_edge(1, 4, 3)
    g.add_edge(4, 3, 1)
    g.add_edge(2, 4, 1.5)
    g.add_edge(3, 2, 0.5)
    g.add_edge(7, 6, 1)
    g.add_edge(6, 7, 1)
    g.add_edge(5, 7, 4)
    g.add_edge(8, 5, 3)
    return g


class TestDiGraph(TestCase):
    def test_v_size(self):
        g = graph_creator()
        v = g.v_size()
        self.assertEqual(10, v)

    def test_e_size(self):
        g = graph_creator()
        self.assertEqual(12, g.e_size())

    def test_get_all_v(self):
        g = graph_creator()
        v = g.get_all_v()
        self.assertEqual(10, v.__len__())

    def test_all_in_edges_of_node(self):
        g = graph_creator()
        v = g.all_in_edges_of_node(0)
        self.assertEqual(1, v.__len__())
        v = g.all_in_edges_of_node(7)
        self.assertEqual(2, v.__len__())

    def test_all_out_edges_of_node(self):
        g = graph_creator()
        v = g.all_out_edges_of_node(0)
        self.assertEqual(2, v.__len__())
        v = g.all_out_edges_of_node(1)
        self.assertEqual(2, v.__len__())

    def test_get_mc(self):
        g = graph_creator()
        self.assertEqual(22, g.get_mc())  # 10 for nodes + 12 for edges

    def test_add_edge(self):
        g = graph_creator()
        g.add_edge(1, 7, 0.5)
        v = g.e_size()
        self.assertEqual(13, v)
        g.add_edge(4, 3, 1)  # an edge that already exists
        v = g.e_size()
        self.assertEqual(13, v)

    def test_add_node(self):
        graph = DiGraph()
        graph.add_node(1, (0.5, 3, 0.0))
        graph.add_node(2, (1, 1, 0))
        self.assertEqual(2, graph.v_size())
        graph.add_node(1, (4, 5, 0.0))
        self.assertNotEqual(3, graph.v_size())

    def test_remove_node(self):
        g = graph_creator()
        g.remove_node(0)
        v = g.v_size()
        e = g.e_size()
        self.assertEqual(9 ,v)
        self.assertEqual(9, e)

    def test_remove_edge(self):
        self.fail()
