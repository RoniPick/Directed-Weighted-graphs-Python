from Location import Location


class Node(Location):

    def __init__(self, id, location: dict):  # data constructor
        self.id = id
        self.weight = 0.0
        self.tag = 0
        self.location = location  # x: location[0], y: location[1], z: location[2]

    def __init__(self, node):  # object constructor
        self.id = node.id
        self.weight = node.weight
        self.tag = node.tag
        self.location = node.location

    def __repr__(self):
        return f"id:{self.id} location:{self.location}"

