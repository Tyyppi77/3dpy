# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import baseobject
import vec3
import application


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
            ),
            baseobject.TexturedCubeObject(
                "img/test_texture1.png",
                position_vector=vec3.Vec3f(0.0, 0.0, -300.0),
                width=-50.0,
                height=-50.0,
                depth=-50.0
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

        glRotatef(0.125, 1.0, 0.125, 0.0)

        for p in self.polygons:
            p.render()

        glutSwapBuffers()


class Test_02(application.Application):
    """
    Creates a test program using the application base class.
    """

    def __init__(self, **kwargs):
        """
        Initializes the application.
        """
        application.Application.__init__(self, **kwargs)

        self.objects = (
            baseobject.TexturedCubeObject(
                "img/test_texture1.png",
                position_vector=vec3.Vec3f(100, 200, 0),
                width=100.0,
                height=100.0,
                depth=100.0
            ),
            baseobject.TexturedCubeObject(
                "img/test_texture1.png",
                position_vector=vec3.Vec3f(0.0, 0.0, -300.0),
                width=-50.0,
                height=-50.0,
                depth=-50.0
            )
        )

        glutMainLoop()

    def draw_scene(self):
        """
        This method is called when the GLUT window needs to drawed.
        """
        glClear(GL_COLOR_BUFFER_BIT)

        glRotatef(0.125, 1.0, 0.125, 0.0)

        for p in self.objects:
            p.render()

        glutSwapBuffers()

    def idle_scene(self):
        """
        This method is called when the GLUT window is in idle mode.
        """
        pass

    def on_mouse_event(self, button_id, state, x, y):
        """
        This method is called when the mouse is clicked.
        """
        pass

    def on_keyboard_event(self, key_char, x, y):
        """
        This method is called when a keyboard button is pressed.
        """
        if key_char == b"\x1b":
            import sys
            sys.exit(0)

    def on_window_reshape(self, width, height):
        """
        This method is called when the window is resized.
        """
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION | GL_MODELVIEW)
        glLoadIdentity()
        glOrtho(-(width / 2), width / 2, height / 2, -(height / 2), -400, 400)

if __name__ == "__main__":
    Test_02(window_title=b"OPENGL")