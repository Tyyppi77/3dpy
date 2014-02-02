# -*- coding: utf-8 -*-
from OpenGL.GL import *

import texture2
import vec3

GL_TEXTURE_COORDINATE_DEFAULTS = [
    vec3.Vec3f(0.0, 0.0, 0.0),
    vec3.Vec3f(0.0, 1.0, 0.0),
    vec3.Vec3f(1.0, 1.0, 0.0),
    vec3.Vec3f(1.0, 0.0, 0.0),
]


class Polygon(object):
    """
    Defines a 2D polygon. The polygon has a list of 3d vectors, that define the
    corners of the polygon. This implementation of the polygon takes in
    also a color, that the polygon will be filled with.
    """

    def __init__(self, vertices=[], normal=None, color=(1.0, 0.0, 0.0)):
        """
        Initializes the polygon
        """
        self.vertices = vertices
        self.normal = normal
        self.color = color

        if not normal:
            self.normal = vec3.Vec3f(-1, -1, -1)

    def add_vertice(self, vector):
        """
        Adds a vector point to the vertice list.
        """
        self.vertices.append(vector)

    def clone(self):
        """
        Clones the polygon and returns the clone
        """
        return Polygon(self.vertices, self.normal, self.color)

    def render(self):
        """
        Renders the polygon. This is not very smart system yet, since it would
        be helpfull if there was a system to order the vertices correctly. Also,
        the GL_POLYGON should be changed to GL_TRIANGLE_STRIP when it is possible.
        """
        glBegin(GL_POLYGON)
        glNormal3d(self.normal.x, self.normal.y, self.normal.z)
        glColor3f(self.color[0], self.color[1], self.color[2])

        #Loops through the vertices drawing them
        for vertice in self.vertices:
            glVertex3d(vertice.x, vertice.y, vertice.z)

        glEnd()

        return True


class TexturedPolygon(Polygon, object):
    """
    Creates a polygon that has a texture binded to it. The texture can be
    loaded earlier, or the init method can handle the loading. The textured polygon
    has a list of the corner points of the polygon, stored in 3d vectors.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the polygon. The *args will take either a filepath
        to the wanted texture, or a previously loaded texture class.
        The **kwargs should get the normal of the polygon, and the vertices
        list.
        """
        Polygon.__init__(self, **kwargs)

        #Checks if the argument got is a filepath
        if len(args) == 1 and type(args[0]) == str:
            self.texture = texture2.Texture2d(args[0])

        #Checks if the argument got is a texture
        elif len(args) == 1 and type(args[0]) == texture2.Texture2d:
            self.texture = args[0]

    def clone(self):
        """
        Clones the polygon
        """
        return Polygon(self.texture, vertices=self.vertices, normal=self.normal)

    def setup_texture(self):
        """
        Sets the texture arguments and binds it before the rendering
        happens. This could be moved to the Texture class, since it would
        be usefull to have an easy way to bind the texture to OpenGL
        from anywhere.
        """
        glEnable(GL_TEXTURE_2D)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

        glBindTexture(GL_TEXTURE_2D, self.texture.id)
        return True

    def render(self):
        """
        Renders the polygon, looping through the vertices. This
        excepts that the vertices are in correct order, since there is no
        system to check if the vertices are in correct order. There should
        also be a system to make the texture coordinates depend on the
        vertices. Also, they are broken currently, the texture is displayed
        upside down.
        """
        self.setup_texture()

        texture_coordinates = GL_TEXTURE_COORDINATE_DEFAULTS

        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glEnable(GL_NORMALIZE)
        glBegin(GL_POLYGON)
        glNormal3d(self.normal.x, self.normal.y, self.normal.z)

        #Loops through the vertices drawing them
        for index, vertice in enumerate(self.vertices):
            glTexCoord2f(texture_coordinates[index].x, texture_coordinates[index].y)
            glVertex3d(vertice.x, vertice.y, vertice.z)

        glEnd()
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_NORMALIZE)

        return True