
# ------------------------------------------------------------
# Class 1 - Task 3
# Generate a 2D rectangle with given dimensions in the
#   given place of the coordinate system. Add some kind
#   of deformation to the rectangle.
#-------------------------------------------------------------

import sys
import random
from math import *
from glfw.GLFW import *
from OpenGL.GL import *

# Generate a color for the rectangle
color = (random.random(), random.random(), random.random())

def startup():
    glClearColor(0.5, 0.5, 0.5, 1.0)
    update_viewport(None, 800, 800)


def shutdown():
    pass


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw a rectangle in a random color, rotated at an angle
    draw_rectangle(0.0, 0.0, 50.0, 50.0, 30.0)

    glFlush()


def draw_rectangle(x, y, a, b, d):
    # x, y - coordinates of the middle of the rectangle
    # a, b - dectangle dimensions (width, height)
    # d - rotation angle of the rectangle

    w1 = (x - a / 2, y + b / 2)
    w2 = (x + a / 2, y + b / 2)
    w3 = (x + a / 2, y - b / 2)
    w4 = (x - a / 2, y - b / 2)

    angle = radians(d)

    # Uncomment this for disco colors
    #color = (random.random(), random.random(), random.random())

    # First triangle
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_TRIANGLES)
    # Vertex 1
    glVertex2f(x + ((w1[0] - x) * cos(angle)) - ((w1[1] - y) * sin(angle)), y + ((w1[0] - x) * sin(angle) + (w1[1] - y) * cos(angle)))
    # Vertex 2
    glVertex2f(x + ((w2[0] - x) * cos(angle)) - ((w2[1] - y) * sin(angle)), y + ((w2[0] - x) * sin(angle) + (w2[1] - y) * cos(angle)))
    # Vertex 3
    glVertex2f(x + ((w3[0] - x) * cos(angle)) - ((w3[1] - y) * sin(angle)), y + ((w3[0] - x) * sin(angle) + (w3[1] - y) * cos(angle)))

    glEnd()

    # Second triangle
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_TRIANGLES)
    # Vertex 1
    glVertex2f(x + ((w1[0] - x) * cos(angle)) - ((w1[1] - y) * sin(angle)), y + ((w1[0] - x) * sin(angle) + (w1[1] - y) * cos(angle)))
    # Vertex 2
    glVertex2f(x + ((w3[0] - x) * cos(angle)) - ((w3[1] - y) * sin(angle)), y + ((w3[0] - x) * sin(angle) + (w3[1] - y) * cos(angle)))
    # Vertex 3
    glVertex2f(x + ((w4[0] - x) * cos(angle)) - ((w4[1] - y) * sin(angle)), y + ((w4[0] - x) * sin(angle) + (w4[1] - y) * cos(angle)))

    glEnd()


def update_viewport(window, width, height):
    if height == 0:
        height = 1
    if width == 0:
        width = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio, 1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0, 1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(800, 800, "Task 3 - a tilted rectangle, in random color", None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport(window, 800, 800))
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
