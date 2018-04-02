from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myInit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1, 1, 1, 1)   # clear background
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10, 10, 10 ,0, 0, 0, 0, 1, 0)

x=0
angle=0
z=0
s=0
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global z
    global s
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3d(40-x, 0,7)
    glVertex3d(-40-x, 0, 7)
    glVertex3d(-40-x, 0, -7)
    glVertex3d(40-x, 0, -7)
    glEnd()
    #Tree
    glColor3f(0.6, 0.3, 0)
    glLoadIdentity()
    glTranslate(-x - 5, 2.5, -8)
    glScale(0.08, 1, 0.08)
    glutSolidCube(5)
    glColor3f(0, 0.6, 0)
    glLoadIdentity()
    glTranslate(-x - 5, 4, -8)
    glScale(1, 1, 1)
    glutSolidSphere(2, 90, 120)
    #first cube
    glLoadIdentity()
    glColor3f(1, 1, 0)
    glTranslate(x,0,0)
    glScale(1,0.25,0.5)
    glutSolidCube(5)

    glLoadIdentity()  #second cube
    glTranslate(x,.25*5,0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

#blue torus
    global angle
    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x+2.5,-2.5*.25,2.5*0.5)
    glRotatef(angle,0,0,1)
    glutWireTorus(0.125,.5,12,8)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x+2.5, -2.5 * .25, -2.5 * 0.5)
    glRotatef(angle, 0, 0, 1)
    glutWireTorus(0.125, .5, 12, 8)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x-2.5, -2.5 * .25, -2.5 * 0.5)
    glRotatef(angle, 0, 0, 1)
    glutWireTorus(0.125, .5, 12, 8)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x-2.5, -2.5 * .25, 2.5 * 0.5)
    glRotatef(angle, 0, 0, 1)
    glutWireTorus(0.125, .5, 12, 8)





#animation
    if (x>7):
        z=1
        x-=.001
        angle+=.1
    elif(x>-14 and z!=0):
        x-=.001
        angle+=.1
    elif(x<-14 ):
        z=0
        x+=.001
        angle-=.1
    else:
        x+=.001
        angle-=.1



    glFlush()




glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Moving_Car_Mahmoud_Products")
glutDisplayFunc(draw)
glutIdleFunc(draw)
myInit()
glutMainLoop()