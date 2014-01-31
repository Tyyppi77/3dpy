import math


class Vec3f(object):

    def __init__(self, *args):
        if len(args) == 1 and type(args[0]) == Vec3f:  # Got a vector in arguments
            self.x = args[0].x
            self.y = args[0].y
            self.z = args[0].z

        elif len(args) == 3:  # Got three integers in arguments
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]

        else:
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
    v = Vec3f()
    assert v.x == 0.0
    assert v.y == 0.0
    assert v.z == 0.0


def test_02():
    v1 = Vec3f()
    v2 = Vec3f()
    v1.x = 1
    v1.y = 1
    v1.z = 1
    v = v1 + v2
    assert v.x == 1.0
    assert v.y == 1.0
    assert v.z == 1.0


def test_03():
    v1 = Vec3f(3, 4, 0)
    v2 = Vec3f(v1)
    assert str(v1) == str(v2)

print(nose.run())  # Just uses the nose once. This should always print OK
