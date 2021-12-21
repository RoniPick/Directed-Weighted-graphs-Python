class Location:

    def __init__(self):  # an empty constructor
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    def __int__(self, first, second, third):  # data constructor
        self.x = first
        self.y = second
        self.z = third

    def __init__(self, location):  # object constructor
        self.x = location.x
        self.y = location.y
        self.z = location.z
