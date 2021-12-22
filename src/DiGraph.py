from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):

    def __init__(self):  # an empty constructor
        self.nodes = {}  # a dictionary of node_id: int -> node_info: Node
        self.out_edges = {}
        """a nested dictionary that represents all the out edges from a node. source:int -> dest:int -> weight:float"""
        self.in_edges = {}
        """a nested dictionary that represents all the in edges to a node. dest:int -> source:int -> weight:float"""
        self.MC = 0  # a counter of all the changes in the graph
        self.nodeSize = 0
        self.edgeSize = 0
    # def __init__(self, graph):  # an object constructor
    #     self.nodes = graph.nodes.copy()
    #     self.out_edges = graph.out_edges.copy()
    #     self.in_edges = graph.in_edges.copy()
    #     self.MC = graph.MC

    def v_size(self) -> int:
        return self.nodeSize

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.in_edges.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.out_edges.get(id1)

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """if the source and the dest are the same or one of them doesn't exist in the graph -> do nothing"""
        if not self.nodes.__contains__(id1) or not self.nodes.__contains__(id2) or id1 == id2:
            return False
        if self.edge_exist(id1, id2):  # if the edge exist in the edge's dictionary -> do nothing
            return False
        """if the edge isn't in the node's dictionary -> we create a new node and add him to the dictionary"""
        self.out_edges[id1][id2] = weight  # add the information to the dictionary in the src, dest location
        self.in_edges[id2][id1] = weight  # add the information to the dictionary in the dest, src location
        self.edgeSize += 1
        self.MC = self.MC + 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:  # if the node id is in the node's dictionary -> do nothing
            return False
        """if the node id isn't in the node's dictionary -> we create a new node and add him to the dictionary"""
        self.nodes[node_id] = Node(node_id, location=pos)
        self.out_edges[node_id] = {}
        self.in_edges[node_id] = {}
        self.nodeSize += 1
        """add a new node to the dictionary with the node_id as his key"""
        self.MC = self.MC + 1  # increase the MC for the change in the graph
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:  # if the node id doesn't exist in the dictionary -> do nothing
            return False
        sizeout = self.all_out_edges_of_node(node_id)
        sizein = self.all_in_edges_of_node(node_id)
        for k in sizeout:  # for all the nodes that have an in edge from the node_id node
            del self.in_edges[k][node_id]  # delete the edge from the in dictionary (dest to src)
            self.edgeSize -= 1

        for j in sizein:
            del self.out_edges[j][node_id]  # delete the edge from the out dictionary (src to dest)
            self.edgeSize -= 1

        self.all_in_edges_of_node(node_id).clear()
        self.all_out_edges_of_node(node_id).clear()
        del self.nodes[node_id]  # delete the node from the dictionary
        self.nodeSize -= 1
        self.MC = self.MC + 1  # increase the MC for the change in the graph

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """if the source and the dest are the same or one of them doesn't exist in the graph -> do nothing"""
        if node_id1 not in self.nodes.keys() or node_id2 not in self.nodes.keys() or node_id1 == node_id2:
            return False
        """if the edge doesn't exist in the edge's dictionary (the destination value isn't in the source dictionary)
        -> do nothing"""
        if node_id2 not in self.out_edges.get(node_id1).keys():
            return False
        del self.out_edges[node_id1][node_id2]  # delete the edge from the out dictionary (src to dest)
        del self.in_edges[node_id2][node_id1]  # delete the edge from the in dictionary (dest to src)
        self.edgeSize -= 1
        self.MC = self.MC + 1  # increase the MC for the change in the graph
        return True

    def edge_exist(self, id1, id2):
        if self.all_out_edges_of_node(id1).__contains__(id2):
            return True
        else:
            return False