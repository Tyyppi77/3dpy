from vec3 import *
from polygon import *

class BaseObject(object):
    """description of class"""
    def __init__(self):
        self.polys = []

    def add_polygon(self, poly):
        self.polys.append(poly)

    def draw(self):
        for p in self.polys:
            p.render()


class CubeObject(BaseObject, object):
    def __init__(self, width = 1.0, height = 1.0, depth = 1.0):
        BaseObject.__init__(self)
        self.verts = []
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                for k in range(-1, 2, 2):
                    v = Vec3f(i*width / 2, j * height / 2, k * depth /2)
                    self.verts.append(v)
        self.poly4(0,1,3,2)
        self.poly4(2,3,7,6)
        self.poly4(6,7,5,4)
        self.poly4(4,5,1,0)
        self.poly4(3,1,5,7)
        self.poly4(0,2,6,4)

    def poly4(self, i1, i2, i3, i4):
        p = Polygon()
        p.add_vertice(self.verts[i1])
        p.add_vertice(self.verts[i2])
        p.add_vertice(self.verts[i3])
        p.add_vertice(self.verts[i4])
        self.polys.append(p)


c = CubeObject(10, 10, 10)

