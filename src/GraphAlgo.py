import json
import math
from typing import List
from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: GraphInterface = None):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name) as f:
                graph = DiGraph()
                data = json.load(f)
            for node in data["nodes"]:
                if "pos" in node:
                    pos = tuple(map(float, str(node["pos"]).split(",")))
                else:
                    pos = None
                graph.add_node(node["id"], (node['pos']['x'], node['pos']['y'], node['pos']['Z']))
            for edge in dict["edges"]:
                graph.connect(edge["src"], edge["dest"], edge["w"])
            self.graph = graph
            return True
        except Exception as exception:
            print(exception)
            return False
        finally:
            file_name.close()  # closing the file

    def save_to_json(self, file_name: str) -> bool:
        with open(file_name, 'w') as file:
            json.dump(self, indent=2, fp=file, default=lambda a: a.__dict__)
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
            Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
            @param id1: The start node id
            @param id2: The end node id
            @return: The distance of the path, a list of the nodes ids that the path goes through
            Example:
    #      >>> from GraphAlgo import GraphAlgo
    #       >>> g_algo = GraphAlgo()
    #        >>> g_algo.addNode(0)
    #        >>> g_algo.addNode(1)
    #        >>> g_algo.addNode(2)
    #        >>> g_algo.addEdge(0,1,1)
    #        >>> g_algo.addEdge(1,2,4)
    #        >>> g_algo.shortestPath(0,1)
    #        (1, [0, 1])
    #        >>> g_algo.shortestPath(0,2)
    #        (5, [0, 1, 2])
            Notes:
            If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
            More info:
            https://en.wikipedia.org/wiki/Dijkstra's_algorithm
            """

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
            Finds the shortest path that visits all the nodes in the list
            :param node_lst: A list of nodes id's
            :return: A list of the nodes id's in the path, and the overall distance
            """

    def centerPoint(self) -> (int, float):
        """
            Finds the node that has the shortest distance to it's farthest node.
            :return: The nodes id, min-maximum distance
            """
        maximum = 0.0
        temp = 0.0
        ans = {}
        for srckey in self.graph.nodes:
            maximum = math.inf * (-1)
            for destkey in self.graph.nodes:
                if srckey != destkey:
                    temp = self.shortest_path_dist(srckey, destkey)
                    if maximum < temp:
                        maximum = temp

            ans[srckey] = maximum

        minimum = math.inf
        minNode = None
        for i in ans:
            if ans[i] < minimum:
                minimum = ans[i]
                minNode = i

        return minNode

    def shortest_path_dist(self, src, dest):
        if self.isconnected() and src != dest:
            shortest = self.DijkstraLength(src)
            return shortest.get(dest)
        return -1

    def isconnected(self) -> bool:
        for nodeid in self.graph.nodes:
            curr = self.graph.nodes[nodeid]
            if not self.BFS(curr):
                return False

        return True

    def BFS(self, key): #////ALMOG TODO
        visited = {}
        # priority

    def DijkstraLength(self, src) -> dict:
        g = DiGraph()
        g = self.graph

    def plot_graph(self) -> None:
        """
            Plots the graph.
            If the nodes have a position, the nodes will be placed there.
            Otherwise, they will be placed in a random but elegant manner.
            @return: None
            """
