import math
import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import time


def graph_creator():
    g = DiGraph()
    for i in range(10):
        g.add_node(i)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 8, 2)
    g.add_edge(9, 0, 1)
    g.add_edge(1, 5, 25)
    g.add_edge(1, 4, 3)
    g.add_edge(4, 3, 1)
    g.add_edge(2, 4, 1.5)
    g.add_edge(3, 2, 0.5)
    g.add_edge(7, 6, 1)
    g.add_edge(6, 7, 1)
    g.add_edge(5, 7, 4)
    g.add_edge(8, 5, 3)
    g.add_edge(2, 1, 5)
    g.add_edge(7, 8, 2.5)
    g.add_edge(5, 9, 1.5)
    return g


def graph_creator_b():
    g = DiGraph()
    for i in range(9):
        g.add_node(i)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 3, 1)
    g.add_edge(3, 4, 1)
    g.add_edge(4, 3, 1)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 8, 1)
    g.add_edge(7, 5, 1)
    g.add_edge(8, 7, 1)
    g.add_edge(8, 6, 1)
    return g


def graph_creator_c():
    g = DiGraph()
    for i in range(5):
        g.add_node(i)
    g.add_edge(0, 2, 1.9)
    g.add_edge(1, 2, 6.8)
    g.add_edge(2, 3, 5.5)
    g.add_edge(3, 4, 2)
    g.add_edge(4, 3, 4.5)
    g.add_edge(4, 0, 1)
    g.add_edge(4, 1, 2.2)
    g.add_edge(0, 1, 8)
    return g


class TestGraphAlgo(unittest.TestCase):

    def test_shortest_path_1(self):
        """
        find the shortest path between:
         1. vertex to his self.
         2. node 9 to node 5
         3. find better path after changing weight in edge
         4. no path exist.
        """
        g = graph_creator()
        graph = GraphAlgo(g)
        x1, y1 = graph.shortest_path(9, 9)  # 1
        x2, y2 = graph.shortest_path(9, 5)  # 2
        g.remove_edge(1, 5)
        g.add_edge(1, 5, 1)
        x3, y3 = graph.shortest_path(9, 5)  # 3
        g.remove_edge(7, 6)
        x4, y4 = graph.shortest_path(4, 6)  # 4
        self.assertEqual(0, x1)
        self.assertEqual(6, x2)
        self.assertEqual(3, x3)
        self.assertEqual(math.inf, x4)

    def test_shortest_path_2(self):
        g = graph_creator()
        graph = GraphAlgo(g)
        x, y = graph.shortest_path(2, 2)  # vertex to his self
        lst = [2]
        self.assertEqual(y, lst)
        lst.clear()
        x, y = graph.shortest_path(0, 6)  # node 0 to node 6
        lst = [0, 8, 5, 7, 6]
        self.assertTrue(y == lst)
        lst.clear()
        g.remove_edge(1, 5)
        g.add_edge(1, 5, 1)
        x, y = graph.shortest_path(0, 6)  # find better path after changing weight in edge
        lst = [0, 1, 5, 7, 6]
        self.assertTrue(y == lst)
        lst.clear()
        g.remove_edge(7, 6)
        x, y = graph.shortest_path(0, 6)  # no path exist
        self.assertEqual(y, [])

    def test_shortest_path_creator_c(self):
        g = graph_creator_c()
        graph = GraphAlgo(g)
        a = graph.shortest_path(0, 1)[0]
        self.assertEqual(8, a)
        a = graph.shortest_path(0, 2)[0]
        self.assertEqual(1.9, a)
        a = graph.shortest_path(0, 3)[0]
        self.assertEqual(7.4, a)
        y = graph.shortest_path(0, 3)[1]  # node 0 to node 3
        lst = [0, 2, 3]
        self.assertTrue(y == lst)
        lst.clear()
        a = graph.shortest_path(0, 4)[0]
        self.assertEqual(9.4, a)
        y = graph.shortest_path(0, 4)[1]  # node 0 to node 4
        lst = [0, 2, 3, 4]
        self.assertTrue(y == lst)

    def test_center_point_creator_c(self):
        g = graph_creator_c()
        graph = GraphAlgo(g)
        x = graph.centerPoint()[0]
        y = graph.centerPoint()[1]
        c = 4
        length = 4.5
        self.assertEqual(c, x)
        self.assertEqual(length, y)

    def test_center_point_0(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("C:/Users/User/Desktop/Ex3/data/A0.json")
        x = g_algo.centerPoint()[0]
        y = g_algo.centerPoint()[1]
        c = 7
        length = 6.806805834715163
        self.assertEqual(c, x)
        self.assertEqual(length, y)

    def test_center_point_1_3(self):
        g_algo1 = GraphAlgo()
        g_algo1.load_from_json("C:/Users/User/Desktop/Ex3/data/A1.json")
        a = g_algo1.centerPoint()
        x1 = a[0]
        y1 = a[1]
        c1 = 8
        length1 = 9.925289024973141
        self.assertEqual(c1, x1)
        self.assertEqual(length1, y1)

        g_algo2 = GraphAlgo()
        g_algo2.load_from_json("C:/Users/User/Desktop/Ex3/data/A2.json")
        x2 = g_algo2.centerPoint()[0]
        y2 = g_algo2.centerPoint()[1]
        c2 = 0
        length2 = 7.819910602212574
        self.assertEqual(c2, x2)
        self.assertEqual(length2, y2)

        g_algo3 = GraphAlgo()
        g_algo3.load_from_json("C:/Users/User/Desktop/Ex3/data/A3.json")
        x3 = g_algo3.centerPoint()[0]
        y3 = g_algo3.centerPoint()[1]
        c3 = 2
        length3 = 8.182236568942237
        self.assertEqual(c3, x3)
        self.assertEqual(length3, y3)

    def test_center_point_4(self):
        g_algo4 = GraphAlgo()
        g_algo4.load_from_json("C:/Users/User/Desktop/Ex3/data/A4.json")
        x4 = g_algo4.centerPoint()[0]
        y4 = g_algo4.centerPoint()[1]
        c4 = 6
        length4 = 8.071366078651435
        self.assertEqual(c4, x4)
        self.assertEqual(length4, y4)

    def test_center_point_5(self):
        g_algo5 = GraphAlgo()
        g_algo5.load_from_json("C:/Users/User/Desktop/Ex3/data/A5.json")
        x5 = g_algo5.centerPoint()[0]
        y5 = g_algo5.centerPoint()[1]
        c5 = 40
        length5 = 9.291743173960954
        self.assertEqual(c5, x5)
        self.assertEqual(length5, y5)


if __name__ == '__main__':
    unittest.main()
