# -*- coding: utf-8 -*-
import math

import vec3


class BoundingBox(object):
    """
    Defines a class for doing 3D collision checking. The box
    has a starting position and a size. The actual checking is
    done using two vectors, one for the starting position of the
    box, and one for the end position.
    """

    def __init__(self, position, width=1.0, height=1.0, depth=1.0):
        """
        Initializes the box.
        """
        self.position = position
        self.size = (width, height, depth)

        #Calculates and stores the start and the end position for the box
        self.min = position
        self.max = vec3.Vec3f(position.x, position.y, position.z)
        self.max += vec3.Vec3f(width, height, depth)

        print(position)

        print(self.min, self.max)

    def __eq__(self, other):
        """
        Implemets the '==' (equals) operator for boxes.
        """
        check_value = 0.0000001
        if math.fabs(self.position.x - other.position.x) > check_value:
            return False
        if math.fabs(self.position.y - other.position.y) > check_value:
            return False
        if math.fabs(self.position.z - other.position.z) > check_value:
            return False
        return True

    def contains(self, other):
        """
        Checks if the other is inside the box.
        """
        if type(other) == vec3.Vec3f:
            #Check if the vector's values are inside the box
            if other.x > self.min.x and other.x < self.max.x:
                if other.y > self.min.y and other.y < self.max.y:
                    if other.z > self.min.z and other.z < self.max.z:
                        return True
            return False

        elif type(other) == BoundingBox:
            #Check if the other box is inside the box
            start = False
            end = False
            if other.min.x > self.min.x and other.min.x < self.max.x:
                if other.min.y > self.min.y and other.min.y < self.max.y:
                    if other.min.z > self.min.z and other.min.z < self.max.z:
                        start = True
            if other.max.x > self.min.x and other.max.x < self.max.x:
                if other.max.y > self.min.y and other.max.y < self.max.y:
                    if other.max.z > self.min.z and other.max.z < self.max.z:
                        end = True
            return start and end


def test_01():
    box = BoundingBox(vec3.Vec3f(0, 0, 0), 100, 100, 100)
    vec = vec3.Vec3f(50, 50, 50)
    assert box.contains(vec) is True


def test_02():
    box = BoundingBox(vec3.Vec3f(0, 0, 0), 100, 100, 100)
    sbox = BoundingBox(vec3.Vec3f(0, 0, 0), 100, 100, 100)
    assert box.contains(sbox) is True