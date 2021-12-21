from unittest import TestCase
from DiGraph import DiGraph
from Node import Node


class TestDiGraph(TestCase):
    def test_v_size(self):
        self.fail()

    def test_e_size(self):
        self.fail()

    def test_get_all_v(self):
        self.fail()

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_all_out_edges_of_node(self):
        self.fail()

    def test_get_mc(self):
        self.fail()

    def test_add_edge(self):
        self.fail()

    def test_add_node(self):
        graph = DiGraph.__init__(self)
        graph.add_node(1, (0.5, 3, 0.0))
        graph.add_node(2, (1, 1, 0))
        self.assertEqual(2, graph.v_size(self))
        graph.add_node(1, (4, 5, 0.0))
        self.assertNotEqual(3, graph.v_size(self))

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()
