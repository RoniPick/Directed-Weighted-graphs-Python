class Edge:

    def __init__(self, source, destination, weight):  # data constructor
        self.src = source
        self.dest = destination
        self.weight = weight
        self.tag = 0

    def __init__(self, edge):  # object constructor
        self.src = edge.src
        self.dest = edge.dest
        self.weight = edge.weight
        self.tag = edge.tag

