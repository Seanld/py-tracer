class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

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

    def __add__(self, otherVector):
        self.x += otherVector.x
        self.y += otherVector.y
        self.z += otherVector.z
    def __sub__(self, otherVector):
        self.x -= otherVector.x
        self.y -= otherVector.y
        self.z -= otherVector.z