# -*- coding: utf-8 -*-
from OpenGL.GL import *

from PIL.Image import open as iopen


class Texture2d(object):
    """
    Defines a class for loading 2d textures from a file. The texture is
    loaded using PIL, and then it's converted to a string format, that GL
    is able to handle. The methods can be called more than once, since
    the id is the only thing that is affected by them
    """

    def __init__(self, filename):
        """
        Initializes the texture, and calls a method to start the loading
        of the texture.
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
        texture_data = texture_file.tostring()

        return self.create_texture(texture_data, texture_size)

    def create_texture(self, texture_data, texture_size):
        """
        Creates the texture to OpenGL. Handles the binding and creation
        of the texture. Returns true if the loading and creation did not fail.
        """
        self._id = glGenTextures(True)  # Creates a texture id for the texture

        #Creates the texture to GL
        glBindTexture(GL_TEXTURE_2D, self.id)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

        glTexImage2D(
            GL_TEXTURE_2D, 0, 3, texture_size[0], texture_size[1], 0,
            GL_RGB, GL_UNSIGNED_BYTE, texture_data
        )
        return True  # The loading succeeded