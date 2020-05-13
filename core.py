# A very naive and basic project dedicated to making a 3D
# rendering engine that displays to the screen.
# |-> Written by Sean Wilkerson @ github.com/Seanld

from math import sin, cos, radians
import numpy



class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.buffer = [[0] * width] * height

    def paint(self, x, y, value):
        self.buffer[y][x] = value



class Camera:
    # position: physical location of camera.
    # screenDistance: distance of the screen from physical location of the camera.
    def __init__(self, position=[-20, 0, 0], space=None, screenDistance=10, screenWidth=200, screenHeight=150):
        self.screen = Screen(screenWidth, screenHeight)

        if space == None:
            self.space = Space()
        else:
            self.space = space

        self.position = position
        self.screenDistance = screenDistance

    # Will iteratively call the render functions of all object instance currently in the space.
    def render(self, spaceToRender):
        for _object in spaceToRender.objects:
            pass # Do rendering math here (maybe put rendering math for each object in its definition, and refer separately.)

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
        self.objects = {}
    
    def addObject(self, id, _object):
        self.objects[id] = _object
    
    def deleteObject(self, id):
        self.objects.pop(id)

    # aPos is starting location, bPos is destination/testing location.
    def checkCollision(self, aPos, bPos):
        pass


    
class Object:
    def __init__(self, position=[0, 0, 0], vertices=[]):
        self.position = position
        self.vertices = vertices

    # Objects' vertices are relative to its position. To get absolute
    # vertices in relation to the space, use this method.
    def absoluteVertices(self):
        _absVertices = []

        for v in self.vertices:
            newV = [
                self.position[0] + v[0],
                self.position[1] + v[1],
                self.position[2] + v[2]
            ]

            _absVertices.append(newV)
        
        return _absVertices



class Square (Object):
    def render(self):
        pass