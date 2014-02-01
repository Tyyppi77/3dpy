# -*- coding: utf-8 -*-
from OpenGL.GL import *

from PIL.Image import open as iopen


class Texture2d(object):
    """
    Defines a class for loading 2d textures from a file.
    """

    def __init__(self, filename):
        """
        Initializes the texture
        """
        self._id = None

        self.load_texture(filename)

    @property
    def id(self):
        """
        Gets the id of the texture
        """
        return self._id

    def load_texture(self, filename):
        """
        Loads the texture from a file
        """
        texture_file = iopen(filename)  # Opens the image file

        texture_size = texture_file.size
        texture_data = texture_file.tostring("raw", "RGBA", 0, -1)

        return self.create_texture(texture_data, texture_size)

    def create_texture(self, texture_data, texture_size):
        """
        Creates the texture to OpenGL
        """
        self._id = glGenTextures(True)  # Creates a texture id for the texture

        #Creates the texture to GL
        glBindTexture(GL_TEXTURE_2D, self.id)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

        glTexImage2D(
            GL_TEXTURE_2D, 0, 3, texture_size[0], texture_size[1], 0,
            GL_RGBA, GL_UNSIGNED_BYTE, texture_data
        )
        return True  # The loading succeeded