from math import sqrt

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distanceTo(self, other):
        return sqrt(pow((self.x - other.x), 2) + pow((self.y - other.y), 2))

    def __add__(self, otherVector):
        self.x += otherVector.x
        self.y += otherVector.y
    def __sub__(self, otherVector):
        self.x -= otherVector.x
        self.y -= otherVector.y

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def distanceTo(self, other):
        return sqrt(pow((self.x - other.x), 2) + pow((self.y - other.y), 2) + pow((self.z - other.z), 2))

    def __add__(self, otherVector):
        self.x += otherVector.x
        self.y += otherVector.y
        self.z += otherVector.z
    def __sub__(self, otherVector):
        self.x -= otherVector.x
        self.y -= otherVector.y
        self.z -= otherVector.z