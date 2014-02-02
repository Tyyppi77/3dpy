# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import baseobject
import vec3


class Test_01(object):
    """
    Creates a test for the project."""

    def __init__(self):
        """
        Initializes the test
        """
        self.init_window()
        self.init_GL()

        #self.polygons = [
            #polygon.TexturedPolygon(
                #"img/test_texture1.png",
                #vertices=(
                    #vec3.Vec3f(0.0, 0.0, 1.0),
                    #vec3.Vec3f(0.5, 0.0, 1.0),
                    #vec3.Vec3f(0.5, 0.5, 1.0),
                    #vec3.Vec3f(0.0, 0.5, 1.0)
                #),
                #normal=vec3.Vec3f(0.0, 0.0, -1.0)
            #),
            #polygon.TexturedPolygon(
                #"img/test_texture1.png",
                #vertices=(
                    #vec3.Vec3f(0.0, 0.0, 1.0),
                    #vec3.Vec3f(-0.5, 0.0, 1.0),
                    #vec3.Vec3f(-0.5, 0.5, 1.0),
                    #vec3.Vec3f(0.0, 0.5, 1.0)
                #),
                #normal=vec3.Vec3f(0.0, 0.0, -1.0)
            #),
        #]

        self.polygons = [
            baseobject.TexturedCubeObject(
                "img/test_texture1.png",
                position_vector=vec3.Vec3f(100, 200, 0),
                width=100.0,
                height=100.0,
                depth=100.0
            )
            ]

        glutMainLoop()

    def on_resize(self, width, height):
        """
        Resizes the window coordinates
        """
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION | GL_MODELVIEW)
        glLoadIdentity()
        glOrtho(-(width / 2), width / 2, height / 2, -(height / 2), -400, 400)

    def init_GL(self):
        """
        Initalizes GL
        """
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glClearDepth(1.0)
        glMatrixMode(GL_PROJECTION | GL_MODELVIEW)
        glLoadIdentity()

    def init_window(self):
        """
        Initializes the window and everything that it needs to initialize
        """
        glutInit()

        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(800, 600)
        glutInitWindowPosition(0, 0)

        self.window = glutCreateWindow(b"OpenGL Test 01")

        glutDisplayFunc(self.draw_scene)
        glutIdleFunc(self.draw_scene)
        glutReshapeFunc(self.on_resize)

    def draw_scene(self):
        """
        Draws the scene to the screen
        """
        glClear(GL_COLOR_BUFFER_BIT)

        glRotatef(0.125, 1.0, 1.0, 1.0)

        for p in self.polygons:
            p.render()

        glutSwapBuffers()


if __name__ == "__main__":
    Test_01()