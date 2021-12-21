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

    # def test_get_all_v(self):
    #     self.fail()
    #
    # def test_all_in_edges_of_node(self):
    #     self.fail()
    #
    # def test_all_out_edges_of_node(self):
    #     self.fail()
    #
    # def test_get_mc(self):
    #     self.fail()
    #
    # def test_add_edge(self):
    #     self.fail()

    def test_add_node(self):
        graph = DiGraph()
        graph.add_node(1, (0.5, 3, 0.0))
        graph.add_node(2, (1, 1, 0))
        self.assertEqual(2, graph.v_size())
        graph.add_node(1, (4, 5, 0.0))
        self.assertNotEqual(3, graph.v_size())
    #
    # def test_remove_node(self):
    #     self.fail()
    #
    # def test_remove_edge(self):
    #     self.fail()
