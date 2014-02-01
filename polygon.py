# -*- coding: utf-8 -*-
from OpenGL.GL import *

import texture2
import vec3

GL_TEXTURE_COORDINATE_DEFAULTS = [
    vec3.Vec3f(0.0, 0.0, 0.0),
    vec3.Vec3f(1.0, 0.0, 0.0),
    vec3.Vec3f(0.0, 1.0, 0.0),
    vec3.Vec3f(1.0, 1.0, 0.0)
]


class Polygon(object):
    """
    Defines a 2D polygon.
    """

    def __init__(self, vertices=[], normal=None, color=(1.0, 0.0, 0.0)):
        """
        Initializes the polygon
        """
        self.vertices = vertices
        self.normal = normal
        self.color = color

    def add_vertice(self, vector):
        """
        Adds a vector point to the vertice list
        """
        self.vertices.append(vector)

    def clone(self):
        """
        Clones the polygon and returns the clone
        """
        return Polygon(self.vertices, self.normal)

    def render(self):
        """
        Renders the polygon
        """
        glBegin(GL_TRIANGLE_STRIP)
        glNormal3d(self.normal.x, self.normal.y, self.normal.z)
        glColor3f(self.color[0], self.color[1], self.color[2])

        #Loops through the vertices drawing them
        for vertice in self.vertices:
            glVertex3d(vertice.x, vertice.y, vertice.z)

        glEnd()

        return True


class TexturedPolygon(Polygon, object):
    """
    Creates a polygon that has a texture binded to it
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the polygon
        """
        Polygon.__init__(self, **kwargs)

        #Checks if the argument got is a filepath
        if len(args) == 1 and type(args[0]) == str:
            self.texture = texture2.Texture2d(args[0])

        #Checks if the argument got is a texture
        elif len(args) == 1 and type(args[0]) == texture2.Texture2d:
            self.texture = args[0]

    def setup_texture(self):
        """
        Sets the texture arguments and binds it before the rendering
        happens.
        """
        glEnable(GL_TEXTURE_2D)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

        glBindTexture(GL_TEXTURE_2D, self.texture.id)
        return True

    def render(self):
        """
        Renders the polygon
        """
        self.setup_texture()

        texture_coordinates = GL_TEXTURE_COORDINATE_DEFAULTS

        glBegin(GL_TRIANGLE_STRIP)
        glNormal3d(self.normal.x, self.normal.y, self.normal.z)

        #Loops through the vertices drawing them
        for index, vertice in enumerate(self.vertices):
            glTexCoord2f(texture_coordinates[index].x, texture_coordinates[index].y)
            glVertex3d(vertice.x, vertice.y, vertice.z)

        glEnd()
        glDisable(GL_TEXTURE_2D)

        return True