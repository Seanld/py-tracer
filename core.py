# A very naive and basic project dedicated to making a 3D
# rendering engine that displays to the screen, via ray-tracing.
# |-> Written by Sean Wilkerson @ github.com/Seanld

from math import sin, cos, radians
from random import randrange
from string import ascii_letters
from vectors import Vector2, Vector3
from numpy import dot

def randomId(length) -> str:
    final = ""
    
    for _ in range(length):
        final += ascii_letters[randrange(0, len(ascii_letters) - 1)]

    return final


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.buffer = [[0] * width] * height

    def paint(self, x, y, value):
        self.buffer[y][x] = value



class ImagePlane:
    def __init__(self, dimensions):
        pass


class Camera:
    # position: physical location of camera.
    # screenDistance: distance of the screen from physical location of the camera.
    def __init__(self, position=[0, 0, -20], space=None, screenDistance=10, screenWidth=200, screenHeight=150):
        self.screen = Screen(screenWidth, screenHeight)

        if space == None:
            self.space = Space()
        else:
            self.space = space

        self.position = position
        self.screenDistance = screenDistance

    # Renders and individual object; kept separate for readability purposes.
    def _renderObject(self, objectToRender):
        pass
    # Will iteratively call the render functions of all object instance currently in the space.
    def render(self):
        for _object in self.objects:
            self._renderObject(self, _object)

    

    # Absolute camera movement.
    def moveTo(self, position):
        self.position = position
    
    # Relative camera movement.
    def moveBy(self, increment):
        self.position[0] += increment[0]
        self.position[1] += increment[1]
        self.position[2] += increment[2]



class Space:
    def __init__(self):
        self.objects = []
    
    def addObject(self, _object):
        self.objects.append(_object)
    
    def deleteObject(self, id):
        i = 0

        while i < (len(self.objects) - 1):
            current = self.objects[i]

            if current.id == id:
                self.objects = self.objects[:i] + self.objects[i+1:]

    # aPos is starting location, bPos is destination/testing location.
    def checkCollision(self, aPos, bPos):
        pass


    
class Object:
    def __init__(self, position=[0, 0, 0], vertices=[], id=""):
        self.position = position
        self.vertices = vertices

        if self.id == "":
            self.id = randomId(8)

    # Objects' vertices are relative to its position. To get absolute
    # vertices in relation to the space, use this method.
    def absoluteVertices(self) -> list:
        _absVertices = []

        for v in self.vertices:
            newV = [
                self.position[0] + v[0],
                self.position[1] + v[1],
                self.position[2] + v[2]
            ]

            _absVertices.append(newV)
        
        return _absVertices



class Ray:
    def __init__(self, origin: Vector3, direction: Vector3):
        self.origin = origin
        self.direction = direction
    
    # Return list-form of directional vector (for dot product via Numpy).
    def asList(self) -> list:
        return [self.direction.x, self.direction.y, self.direction.z]

        

class Sphere (Object):
    def __init__(self, position: Vector3, radius: float):
        self.position = position
        self.radius = radius
    
    # Check if `ray` intersects with Sphere.
    def intersect(self, ray) -> bool:
        rayAsList: list = ray.asList()

        # Distance from ray's origin (camera position likely), to position of sphere.
        distOriginToSphere: Vector3 = ray.origin - self.position

        # d.d -- Vector dot-product of the direction.
        A: float = dot(rayAsList, rayAsList)
        # 2d.(p0 - c)
        B: float = 2 * dot(rayAsList, distOriginToSphere)
        # (p0 - c).(p0 - c) - r^2
        C: float = dot(distOriginToSphere, distOriginToSphere) - (self.radius ** 2)

        # The discriminant.
        discrim: float = B * B - 4 * A * C

        if discrim < 0:
            return False
        else:
            return True