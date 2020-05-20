# A very naive and basic project dedicated to making a 3D
# rendering engine that displays to the screen, via ray-tracing.
# |-> Written by Sean Wilkerson @ github.com/Seanld

from math import sin, cos, radians
from random import randrange
from string import ascii_letters
from vectors import Vector2, Vector3
from numpy import dot
from typing import List

def randomId(length) -> str:
    final = ""
    
    for _ in range(length):
        final += ascii_letters[randrange(0, len(ascii_letters) - 1)]

    return final


class ImagePlane:
    # position: center of the plane
    # resolution: how many pixels wide and tall the plane is
    def __init__(self, position: Vector3, size: Vector2, resolution = None):
        self.position = position
        if resolution == None:
            self.resolution = size
        else:
            self.resolution = resolution
        self.size = size
        self.pixelSize = Vector2(size.x / self.resolution.x, size.y / self.resolution.y)
    
    def getPixelPositions(self) -> List[Vector3]:
        Y = (self.position.y - (self.size.x / 2)) + (self.pixelSize.x / 2)
        Z = (self.position.z + (self.size.y / 2)) - (self.pixelSize.y / 2)
        startingPoint = Vector3(self.position.x, Y, Z)

        pixelPositions: List[List[Vector3]] = []

        for z in range(self.resolution.y):
            row: List[Vector3] = []

            for y in range(self.resolution.x):
                temp = Vector3(0, startingPoint.y + (y * self.pixelSize.x), startingPoint.z - (z * self.pixelSize.y))
                row.append(temp)
            
            pixelPositions.append(row)
        
        return pixelPositions


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


class Camera:
    # position: physical location of camera.
    # screenDistance: distance of the screen from physical location of the camera.
    def __init__(self, position: Vector3 = Vector3(), space: Space= None,
        screenDistance: float = 10, screenRes: Vector2 = Vector2(100, 100),
        screenSize: Vector2 = Vector2(100, 100)):
        if space == None:
            self.space = Space()
        else:
            self.space = space

        self.position = position
        self.screenDistance = screenDistance
        self.buffer = [[0] * screenRes.x] * screenRes.y
        self.screen = ImagePlane(Vector3(self.position.x + self.screenDistance, self.position.y, self.position.z), screenSize, screenRes)

    # Renders and individual object; kept separate for readability purposes.
    def _renderObject(self, objectToRender):
        pass
    # Will iteratively call the render functions of all object instance currently in the space.
    def render(self):
        for _object in self.objects:
            self._renderObject(self, _object)

    

    # Absolute camera movement.
    def moveTo(self, position: Vector3):
        self.position = position
        self.screen.position = Vector3(self.position.x + self.screenDistance, self.position.y, self.position.z)
    
    # Relative camera movement.
    def moveBy(self, increment: Vector3):
        self.position += increment
        self.screen.position = Vector3(self.position.x + self.screenDistance, self.position.y, self.position.z)

    
class Object:
    def __init__(self, position: Vector3 = Vector3(), vertices: List[Vector3] = [], id=""):
        self.position = position
        self.vertices = vertices

        if self.id == "":
            self.id = randomId(8)

    # Objects' vertices are relative to its position. To get absolute
    # vertices in relation to the space, use this method.
    def absoluteVertices(self) -> List[Vector3]:
        _absVertices = []

        for v in self.vertices:
            temp = Vector3(self.position.x + v.x, self.position.y + v.y, self.position.z + v.z)

            _absVertices.append(temp)
        
        return _absVertices



class Ray:
    def __init__(self, origin: Vector3, direction: Vector3):
        self.origin = origin
        self.direction = direction



class Sphere (Object):
    def __init__(self, position: Vector3, radius: float):
        self.position = position
        self.radius = radius
    
    # Check if `ray` intersects with Sphere.
    def intersect(self, ray) -> bool:
        rayAsList: list = ray.direction.asList()
        
        # Distance from ray's origin (camera position likely), to position of sphere.
        distOriginToSphere: Vector3 = ray.origin - self.position
        distOriginToSphere = distOriginToSphere.asList()

        print(distOriginToSphere)

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