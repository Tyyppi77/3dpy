import math

class vec3f(object):
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __mul__(self, other):
        self.x *= other
        self.y *= other
        self.z *= other
        return self

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    @property
    def length(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    @property
    def length_sq(self):
        return math.sqrt(self.length)

    def normalize(self):
        rcp = 1 / self.length
        self.x *= rcp
        self.y *= rcp
        self.z *= rcp

    def __str__(self):
        return "%.6f %.6f %.6f" % (self.x, self.y, self.z)


import nose

def test_01():
    v = vec3f()
    assert v.x == 0.0
    assert v.y == 0.0
    assert v.z == 0.0

def test_02():
    v1 = vec3f()
    v2 = vec3f()
    v1.x = 1
    v1.y = 1
    v1.z = 1
    v = v1 + v2
    assert v.x == 1.0
    assert v.y == 1.0
    assert v.z == 1.0
