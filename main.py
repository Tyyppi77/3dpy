# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import vec3
import polygon


class Test_01(object):
    """
    Creates a test for the project."""

    def __init__(self):
        """
        Initializes the test
        """
        self.init_window()
        self.init_GL()

        self.polygons = [
            polygon.TexturedPolygon(
                "img/test_texture.png",
                vertices=(
                    vec3.Vec3f(0.0, 0.0, 0.0),
                    vec3.Vec3f(0.5, 0.0, 0.0),
                    vec3.Vec3f(0.5, 0.5, 0.0),
                    vec3.Vec3f(0.0, 0.5, 0.0)
                ),
                normal=vec3.Vec3f(0.0, 0.0, 1.0)
            )
        ]

        glutMainLoop()

    def init_GL(self):
        """
        Initalizes GL
        """
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glMatrixMode(GL_PROJECTION | GL_MODELVIEW)
        glLoadIdentity()

    def init_window(self):
        """
        Initializes the window and everything that it needs to initialize
        """
        glutInit(1, ["foo"])

        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(700, 500)
        glutInitWindowPosition(0, 0)

        self.window = glutCreateWindow(b"OpenGL Test 01")

        glutDisplayFunc(self.draw_scene)
        glutIdleFunc(self.draw_scene)

    def draw_scene(self):
        """
        Draws the scene to the screen
        """
        glClear(GL_COLOR_BUFFER_BIT)

        for p in self.polygons:
            p.render()

        glutSwapBuffers()


if __name__ == "__main__":
    Test_01()