from src.GraphInterface import GraphInterface
from Node import Node
from Edge import Edge


class DiGraph(GraphInterface):

    def __init__(self):  # an empty constructor
        self.nodes = {}  # a dictionary of node_id: int -> node_info: Node
        self.out_edges = {}
        """a nested dictionary that represents all the out edges from a node. source:int -> dest:int -> weight:float"""
        self.in_edges = {}
        """a nested dictionary that represents all the in edges to a node. dest:int -> source:int -> weight:float"""
        self.MC = 0  # a counter of all the changes in the graph

    def __int__(self, graph):  # an object constructor
        self.nodes = graph.nodes.copy()
        self.out_edges = graph.out_edges.copy()
        self.in_edges = graph.in_edges.copy()
        self.MC = graph.MC

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        ans = 0
        for k, v in self.out_edges.items():
            ans = ans + len(v)
        return ans

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.in_edges[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.out_edges[id1]

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """if the source and the dest are the same or one of them doesn't exist in the graph -> do nothing"""
        if id1 not in self.nodes.keys() or id2 not in self.nodes.keys() or id1 == id2:
            return False
        if id2 in self.out_edges.get(id1).keys():  # if the edge exist in the edge's dictionary -> do nothing
            return False ## 1:3 1:
        """if the edge isn't in the node's dictionary -> we create a new node and add him to the dictionary"""
        self.out_edges[id1][id2] = weight  # add the information to the dictionary in the src, dest location
        self.in_edges[id2][id1] = weight  # add the information to the dictionary in the dest, src location
        self.MC = self.MC + 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:  # if the node id is in the node's dictionary -> do nothing
            return False
        """if the node id isn't in the node's dictionary -> we create a new node and add him to the dictionary"""
        self.nodes[node_id] = Node(node_id, {'x': pos[0], 'y': pos[1], 'z': pos[2]})
        """add a new node to the dictionary with the node_id as his key"""
        self.MC = self.MC + 1  # increase the MC for the change in the graph
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:  # if the node id doesn't exist in the dictionary -> do nothing
            return False
        for k in self.out_edges[node_id]:  # for all the nodes that have an in edge from the node_id node
            self.remove_edge(node_id, k)  # delete all the edges
        del self.nodes[node_id]  # delete the node from the dictionary
        self.MC = self.MC + 1  # increase the MC for the change in the graph

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """if the source and the dest are the same or one of them doesn't exist in the graph -> do nothing"""
        if node_id1 not in self.nodes.keys() or node_id2 not in self.nodes.keys() or node_id1 == node_id2:
            return False
        """if the edge doesn't exist in the edge's dictionary (the destination value isn't in the source dictionary)
        -> do nothing"""
        if node_id2 not in self.nodes.get(node_id1).keys():
            return False
        del self.out_edges[node_id1][node_id2]  # delete the edge from the out dictionary (src to dest)
        del self.in_edges[node_id2][node_id1]  # delete the edge from the in dictionary (dest to src)
        self.MC = self.MC + 1  # increase the MC for the change in the graph
        return True

