from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np
from math import *




def draw_Head():
    glBegin(GL_POLYGON)
    glColor3f(0.2,0,0.5)

    glVertex(0.07,0.5)
    glVertex(0.07,0.65)
    glVertex(-0.07,0.65)
    glVertex(-0.07,0.5)


    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1,0.9,0.3)
    glVertex(0.18, 0.65)
    glVertex(0.18, 0.97)
    glVertex(-0.18, 0.97)
    glVertex(-0.18, 0.65)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0.4)
    glVertex(0.18, 0.65)
    glVertex(0.18, 0.97)
    glVertex(-0.18, 0.97)
    glVertex(-0.18, 0.65)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0,0,0.4)

    glVertex(0.22,0.85)
    glVertex(0.22,0.9)
    glVertex(0.18,0.9)
    glVertex(0.18,0.85)

    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0,0,0.4)

    glVertex(-0.22,0.85)
    glVertex(-0.22,0.9)
    glVertex(-0.18,0.9)
    glVertex(-0.18,0.85)

    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0,0,0.4)
    glVertex(0.18,0.97)
    glVertex(0,1)
    glVertex(-0.18,0.97)
    glEnd()


    glFlush()


def draw_Eyes_1(r=0.5,xc=0,yc=0):
    glBegin(GL_POLYGON)
    glColor3f(0.5,0.7,0.9)
    for theta in np.arange(0, 2 * pi, 0.01):
        x = xc + r * cos(theta)
        y = yc + r * sin(theta)
        glVertex(x, y)

    glEnd()

def draw_Eyes_2(r=0.5,xc=0,yc=0):
    glBegin(GL_POLYGON)
    glColor3f(0,0,0.4)
    for theta in np.arange(0, 2 * pi, 0.01):
        x = xc + r * cos(theta)
        y = yc + r * sin(theta)
        glVertex(x, y)

    glEnd()

def draw_Eyes_3(r=0.5,xc=0,yc=0):
    glBegin(GL_POLYGON)
    glColor3f(1,0.5,0.8)
    for theta in np.arange(pi, 2 * pi, 0.01):
        x = xc + r * cos(theta)
        y = yc + r * sin(theta)
        glVertex(x, y)

    glEnd()

def draw_Eyes_4(r=0.5,xc=0,yc=0):
    glBegin(GL_POLYGON)
    glColor3f(1,0.2,0.5)
    for theta in np.arange(0, pi, 0.01):
        x = xc + r * cos(theta)
        y = yc + r * sin(theta)
        glVertex(x, y)

    glEnd()

def draw_Eyes_5(r=0.5,xc=0,yc=0):
    glBegin(GL_POLYGON)
    glColor3f(1,0.1,0.3)
    for theta in np.arange(0, 2 * pi, 0.01):
        x = xc + r * cos(theta)
        y = yc + r * sin(theta)
        glVertex(x, y)

    glEnd()

def draw_Leg():
    glBegin(GL_POLYGON)
    glColor3f(0,0,0.4)

    glVertex(0.5,-0.61)
    glVertex(0.5,-0.58)
    glVertex(0.4,-0.58)
    glVertex(0.4,-0.61)

    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0,0,0.4)

    glVertex(-0.5,-0.61)
    glVertex(-0.5,-0.58)
    glVertex(-0.4,-0.58)
    glVertex(-0.4,-0.61)

    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0.9,0.3)

    glVertex(0.4,-0.65)
    glVertex(0.4,-0.5)
    glVertex(0.2,-0.5)

    glVertex(-0.4, -0.65)
    glVertex(-0.4, -0.5)
    glVertex(-0.2, -0.5)

    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(0, 0, 0.4)
    glVertex(0.4, -0.65)
    glVertex(0.4, -0.5)
    glVertex(0.2, -0.5)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(0, 0, 0.4)
    glVertex(-0.4, -0.65)
    glVertex(-0.4, -0.5)
    glVertex(-0.2, -0.5)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0,0,0.4)
    glVertex(0.4,-0.5)
    glVertex(0.4,-0.475)
    glVertex(-0.4,-0.475)
    glVertex(-0.4,-0.5)
    glEnd()

    glBegin(GL_POLYGON)  #last line
    glColor3f(0,0,0.4)
    glVertex(0.4,0.25)
    glVertex(0.4,0.265)
    glVertex(-0.4,0.265)
    glVertex(-0.4,0.25)
    glEnd()



    glBegin(GL_POLYGON)
    glColor3f(0,0,0.4)
    glVertex(0.215,0.25)
    glVertex(0.215,0.5)
    glVertex(0.2,0.5)
    glVertex(0.2,0.25)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0.4)
    glVertex(-0.215, 0.25)
    glVertex(-0.215, 0.5)
    glVertex(-0.2, 0.5)
    glVertex(-0.2, 0.25)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.7, 0.9)
    glVertex(0.55, 0.23)
    glVertex(0.55, 0.31)
    glVertex(0.18, 0.31)
    glVertex(0.18, 0.23)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0.4)
    glVertex(0.55, 0.23)
    glVertex(0.55, 0.31)
    glVertex(0.18, 0.31)
    glVertex(0.18, 0.23)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.7, 0.9)
    glVertex(0.55, 0.1)
    glVertex(0.55, 0.18)
    glVertex(0.18, 0.18)
    glVertex(0.18, 0.1)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0.4)
    glVertex(0.55, 0.1)
    glVertex(0.55, 0.18)
    glVertex(0.18, 0.18)
    glVertex(0.18, 0.1)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.7, 0.9)
    glVertex(0.55, 0.14)
    glVertex(0.55, 0.27)
    glVertex(0.5, 0.27)
    glVertex(0.5, 0.14)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0.4)
    glVertex(0.55, 0.14)
    glVertex(0.55, 0.27)
    glVertex(0.5, 0.27)
    glVertex(0.5, 0.14)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.7, 0.9)
    glVertex(-0.55, 0.23)
    glVertex(-0.55, 0.31)
    glVertex(-0.18, 0.31)
    glVertex(-0.18, 0.23)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0.4)
    glVertex(-0.55, 0.23)
    glVertex(-0.55, 0.31)
    glVertex(-0.18, 0.31)
    glVertex(-0.18, 0.23)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.7, 0.9)
    glVertex(-0.55, 0.1)
    glVertex(-0.55, 0.18)
    glVertex(-0.18, 0.18)
    glVertex(-0.18, 0.1)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0.4)
    glVertex(-0.55, 0.1)
    glVertex(-0.55, 0.18)
    glVertex(-0.18, 0.18)
    glVertex(-0.18, 0.1)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.7, 0.9)
    glVertex(-0.55, 0.14)
    glVertex(-0.55, 0.27)
    glVertex(-0.5, 0.27)
    glVertex(-0.5, 0.14)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0.4)
    glVertex(-0.55, 0.14)
    glVertex(-0.55, 0.27)
    glVertex(-0.5, 0.27)
    glVertex(-0.5, 0.14)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.5, 0.5)
    glVertex(0.2, 0.1835)
    glVertex(0.2, 0.228)
    glVertex(0.497, 0.228)
    glVertex(0.497, 0.1835)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0.4)
    glVertex(0.2, 0.1835)
    glVertex(0.2, 0.228)
    glVertex(0.497, 0.228)
    glVertex(0.497, 0.1835)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.5, 0.5)
    glVertex(-0.2, 0.1835)
    glVertex(-0.2, 0.228)
    glVertex(-0.5, 0.228)
    glVertex(-0.5, 0.1835)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0.4)
    glVertex(-.2, 0.1835)
    glVertex(-0.2, 0.228)
    glVertex(-0.5, 0.228)
    glVertex(-0.5, 0.1835)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0.4)
    glVertex(0.313, 0.23)
    glVertex(0.313, 0.31)
    glVertex(0.3, 0.31)
    glVertex(0.3, 0.23)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0.4)
    glVertex(0.313, 0.1)
    glVertex(0.313, 0.1835)
    glVertex(0.3, 0.1835)
    glVertex(0.3, 0.1)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0.4)
    glVertex(-0.313, 0.23)
    glVertex(-0.313, 0.31)
    glVertex(-0.3, 0.31)
    glVertex(-0.3, 0.23)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0.4)
    glVertex(-0.313, 0.1)
    glVertex(-0.313, 0.1835)
    glVertex(-0.3, 0.1835)
    glVertex(-0.3, 0.1)
    glEnd()


    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0.4)
    glVertex(0.4, 0.4)
    glVertex(0.4, 0.415)
    glVertex(0.215, 0.415)
    glVertex(0.215, 0.4)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0.4)
    glVertex(-0.4, 0.4)
    glVertex(-0.4, 0.415)
    glVertex(-0.215, 0.415)
    glVertex(-0.215, 0.4)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(0.8,-0.78)
    glVertex(0.8,-0.30)
    glVertex(0.5,-0.30)
    glVertex(0.5,-0.78)
    glEnd()


    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.5,-0.78)
    glVertex(-0.5,-0.30)
    glVertex(-0.8,-0.30)
    glVertex(-0.8,-0.78)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)
    glVertex(0.8,-0.72)
    glVertex(0.8,-0.75)
    glVertex(0.5,-0.75)
    glVertex(0.5,-0.72)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)
    glVertex(0.8,-0.65)
    glVertex(0.8,-0.68)
    glVertex(0.5,-0.68)
    glVertex(0.5,-0.65)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)

    glVertex(0.8,-0.58)
    glVertex(0.8,-0.61)
    glVertex(0.5,-0.61)
    glVertex(0.5,-0.58)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)
    glVertex(0.8,-0.51)
    glVertex(0.8,-0.54)
    glVertex(0.5,-0.54)
    glVertex(0.5,-0.51)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)
    glVertex(0.8,-0.44)
    glVertex(0.8,-0.47)
    glVertex(0.5,-0.47)
    glVertex(0.5,-0.44)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)
    glVertex(0.8,-0.37)
    glVertex(0.8,-0.40)
    glVertex(0.5,-0.40)
    glVertex(0.5,-0.37)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)
    glVertex(0.8,-0.32)
    glVertex(0.8,-0.34)
    glVertex(0.5,-0.34)
    glVertex(0.5,-0.32)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)
    glVertex(-0.8,-0.72)
    glVertex(-0.8,-0.75)
    glVertex(-0.5,-0.75)
    glVertex(-0.5,-0.72)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)
    glVertex(-0.8,-0.65)
    glVertex(-0.8,-0.68)
    glVertex(-0.5,-0.68)
    glVertex(-0.5,-0.65)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)

    glVertex(-0.8,-0.58)
    glVertex(-0.8,-0.61)
    glVertex(-0.5,-0.61)
    glVertex(-0.5,-0.58)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)
    glVertex(-0.8,-0.51)
    glVertex(-0.8,-0.54)
    glVertex(-0.5,-0.54)
    glVertex(-0.5,-0.51)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)
    glVertex(-0.8,-0.44)
    glVertex(-0.8,-0.47)
    glVertex(-0.5,-0.47)
    glVertex(-0.5,-0.44)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)
    glVertex(-0.8,-0.37)
    glVertex(-0.8,-0.40)
    glVertex(-0.5,-0.40)
    glVertex(-0.5,-0.37)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0.4)
    glVertex(-0.8,-0.32)
    glVertex(-0.8,-0.34)
    glVertex(-0.5,-0.34)
    glVertex(-0.5,-0.32)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,0.4)
    glVertex(0.93,-0.83)
    glVertex(-0.93,-0.83)
    glVertex(0.6,-0.9)
    glVertex(-0.6,-0.9)
    glVertex(0.3,-0.97)
    glVertex(-0.3,-0.97)
    glEnd()



    glFlush()


def draw_Loop():

    glBegin(GL_POLYGON)
    glColor3f(1, 0.9, 0.3)

    glVertex(0.4, -0.5)
    glVertex(0.4, 0.5)
    glVertex(-0.4, 0.5)
    glVertex(-0.4, -0.5)

    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3f(0.1,0,0)

    glVertex(0.4,-0.5)
    glVertex(0.4,0.5)
    glVertex(-0.4,0.5)
    glVertex(-0.4,-0.5)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 0.5)
    glVertex(0.1, -0.4)
    glVertex(0.1, 0.2)
    glVertex(-0.35, 0.2)
    glVertex(-0.35, -0.4)

    glEnd()




    glFlush()



def axis():
    glColor3f(0, 0, 1)
    glBegin(GL_LINES)
    glVertex(0, -1)
    glVertex(0, 1)
    glVertex(1, 0)
    glVertex(-1, 0)
    glEnd()

def draw():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)

    #axis()


    draw_Loop()
    draw_Head()
    draw_Eyes_1(0.082,0.3,0.875)
    draw_Eyes_1(0.082,-0.3,0.875)
    draw_Eyes_2(0.050,0.332,0.875)
    draw_Eyes_2(0.050,-0.332,0.875)
    draw_Leg()
    draw_Eyes_2(0.012,0.37,-0.59)
    draw_Eyes_2(0.012,-0.37,-0.59)
    draw_Eyes_2(0.011,0.95,-0.83)
    draw_Eyes_2(0.011,-0.95,-0.83)
    draw_Eyes_2(0.011,-0.62,-0.9)
    draw_Eyes_2(0.011,0.62,-0.9)
    draw_Eyes_2(0.011,0.32,-0.97)
    draw_Eyes_2(0.011,-0.32,-0.97)
    draw_Eyes_3(0.1, 0, 0.8)
    draw_Eyes_4(0.05, 0, 0.7053)
    draw_Eyes_5(0.04,0,0.38)







    glFlush()




glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"First OpenGL program")
glutDisplayFunc(draw)
glutMainLoop()

