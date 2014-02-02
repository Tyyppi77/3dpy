# -*- coding: utf-8 -*-
import math


class Vec3f(object):
    """
    Defines a class for 3d vector. This class also handles
    all the vector math that is required.
    """

    def __init__(self, *args):
        """
        Initializes the vector. In the *args there is either a vector,
        that's values will be copied, or three floats that will be
        assigned to their correct variables. If no arguments were got,
        the vector is initialized with 3 zeros.
        """
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
        """
        Implements addition between vectors
        """
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other):
        """
        Implements subtraction between vectors
        """
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __mul__(self, other):
        """
        Implements multiplication
        """
        self.x *= other
        self.y *= other
        self.z *= other
        return self

    def __eq__(self, other):
        """
        Checks if a vector is equal to other vector
        """
        check_value = 0.0000001
        if math.fabs(self.x - other.x) > check_value:
            return False
        if math.fabs(self.y - other.y) > check_value:
            return False
        if math.fabs(self.z - other.z) > check_value:
            return False
        return True

    def dot(self, other):
        """
        Calculates the dot-product between to vectors
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    @staticmethod
    def cross(self, other):
        """
        Calculates the cross-product between to vectors and returns
        it as a new vector
        """
        res = Vec3f()
        res.x = self.y * other.z - self.z * other.y
        res.y = self.z * other.x - self.x * other.z
        res.z = self.x * other.y - self.y * other.x
        return res

    @property
    def length(self):
        """
        Calculates the lenght of the vector. Note that this is un-squarerooted
        so this basicaly equals to self.lenght_sq ** 2.
        """
        return self.x * self.x + self.y * self.y + self.z * self.z

    @property
    def length_sq(self):
        """
        Transforms the lenght to a actual lenght of the vector.
        """
        return math.sqrt(self.length)

    def normalize(self):
        """
        Normalizes the vector
        """
        rcp = 1 / self.length
        self.x *= rcp
        self.y *= rcp
        self.z *= rcp

    def __str__(self):
        """
        Returns the vector's coordinates in a string
        """
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
    assert v1 == v2

if __name__ == "__main__":
    print(nose.run())  # Just uses the nose once. This should always print OK
