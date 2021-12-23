import json
import math
import queue
from typing import List
from src import GraphInterface
from src.DiGraph import DiGraph
from src.Node import Node
from src.GraphAlgoInterface import GraphAlgoInterface
import matplotlib.pyplot as plt
from queue import PriorityQueue


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph() = DiGraph()):
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
        dijkstra = self.Dijkstra(id1)
        dist = dijkstra[0]
        pointers = dijkstra[1]
        temp = id2
        ans = []
        while temp != id1:  # inserting the nodes in the correct order
            ans.insert(0, temp)
            temp = pointers.get(temp)

        ans.insert(0, id1)  # adding the first node to the list
        return dist.get(id2), ans

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
        length = {}  # for the node's Dijkstra
        ans = {}
        for srckey in self.get_graph().nodes.keys():
            maximum = math.inf * (-1)
            length = self.Dijkstra(srckey)[0]  # the dictionary of the length
            for destkey in length.values():
                if maximum < destkey:
                    maximum = destkey

            ans[srckey] = maximum

        minimum = math.inf
        minNode = None
        for i in ans:
            if ans[i] < minimum:
                minimum = ans[i]
                minNode = i

        return minNode, minimum

    def Dijkstra(self, src):
        self.reset()  # resetting the values of the node's tag and weight before applying a new Dijkstra
        dist = {}  # a dictionary of distance from src to the nodeid in the dictionary
        prev = {}
        neighbours = queue.PriorityQueue(maxsize=0)  # maxsize = 0 -> no limit on the length
        dist[src] = 0  # distance from node to itself = 0
        prev[src] = None  # there is no pointer to the node
        neighbours.put(src)
        self.get_graph().get_all_v().get(src).tag = 1  # marked as visited
        while not neighbours.empty():
            temp = neighbours.get()  # temp value - int
            for nodeid in self.get_graph().all_out_edges_of_node(temp).keys():
                if self.relax(temp, nodeid):
                    dist[nodeid] = self.get_graph().get_all_v().get(nodeid).weight  # if we could update - updating the weight of the node int the dict
                    prev[nodeid] = temp  # temp pointing to nodeid
                if self.get_graph().get_all_v().get(nodeid).tag == 0:
                    self.get_graph().get_all_v().get(nodeid).tag = 1  # marked as visited
                    neighbours.put(nodeid)  # adding it to the queue
        return dist, prev

    def relax(self, src: int, dest: int) -> bool:
        srcweight = self.get_graph().get_all_v().get(src).weight
        edgeweight = self.get_graph().all_out_edges_of_node(src).get(dest)

        if self.get_graph().get_all_v().get(dest).weight <= srcweight + edgeweight:
            return False

        self.get_graph().get_all_v().get(dest).weight = srcweight + edgeweight
        return True

    def reset(self):
        for node in self.get_graph().get_all_v().values():
            node.tag = 0
            node.weight = math.inf

    def plot_graph(self) -> None:
        """
            Plots the graph.
            If the nodes have a position, the nodes will be placed there.
            Otherwise, they will be placed in a random but elegant manner.
            @return: None
            """
        x = [1, 2, 3]
        y = [2, 4, 1]
        plt.plot(x, y, color='indigo', linestyle='-', linewidth=2, marker='o', markerfacecolor='gray', markersize=15)
        plt.xlim()
        plt.ylim()
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('OOP Ex3')
        plt.show()

    # if __name__ == "__main__":


