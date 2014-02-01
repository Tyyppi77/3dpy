# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Application(object):
    """
    Defines a base class for any OpenGL GLUT application.
    Every program that needs a window should be inherited from
    this and then the inherited class can redefine some of the
    functions the base class calls. An example would be that the
    inherited class implements a method called 'draw_scene',
    that will be called by GLUT.
    """

    def __init__(self, window_title="", window_size=(800, 600), window_pos=(0, 0)):
        """
        Initializes the application. This should be called always from
        the inherited class, since this calls very important initializing
        functions. This also creates a window for the application.
        """
        #Initalizes GLUT and window
        glutInit()

        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(window_size[0], window_size[1])
        glutInitWindowPosition(window_pos[0], window_pos[1])

        #Creates the window
        self.window = glutCreateWindow(window_title)

        glutDisplayFunc(self.draw_scene)
        glutIdleFunc(self.idle_scene)

        self.initGL()

    def initGL(self):
        """
        Initalizes OpenGL. This method can be reimplemented in child
        class, but it is also suggested that this method is called
        even if it's defined in child class.
        """
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glClearDepth(1.0)
        glMatrixMode(GL_PROJECTION | GL_MODELVIEW)
        glLoadIdentity()

    def draw_scene(self):
        """
        This method is called when the GLUT window needs to drawed.
        This method should be reimplemented in a child class, since
        not doing so will broke the application. This method is where all
        all the drawing needs to happen.
        """
        raise NotImplementedError()

    def idle_scene(self):
        """
        This method is called when the GLUT window is in idle mode.
        This method should be reimplemented in a child class, since
        not doing so will broke the application. This method can simply
        call draw_scene, if it is wanted so.
        """
        raise NotImplementedError()