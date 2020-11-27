
# ------------------------------------------------------------
# Class 1 - Task 4
# Generate a fractal (Sierpinski's Carpet)
#-------------------------------------------------------------

import sys

from glfw.GLFW import *
from OpenGL.GL import *


def startup():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    update_viewport(None, 800, 800)


def shutdown():
    pass


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    drawSierpinski(0.0, 0.0, 180.0, 2.0)

    glFlush()


def drawSquare(x, y, size, color):
    # x, y - coordinates of the middle of the square
    # size - length of the square's side
    # color - color of the square

    glColor3f(color, color, color)
    glBegin(GL_TRIANGLES)

    glVertex2f(x - size / 2, y + size / 2)
    glVertex2f(x + size / 2, y + size / 2)
    glVertex2f(x + size / 2, y - size / 2)

    glEnd()

    glColor3f(color, color, color)
    glBegin(GL_TRIANGLES)

    glVertex2f(x - size / 2, y + size / 2)
    glVertex2f(x + size / 2, y - size / 2)
    glVertex2f(x - size / 2, y - size / 2)

    glEnd()


def drawSierpinski(x, y, size, min):
    # x, y - the middle of Sierpinski's Carpet
    # size - size of the Carpet
    # min - the size of the smallest square

    # Draw the big square
    drawSquare(x, y, size, 1.0)

    # Remove middle
    drawSquare(x, y, size/3, 0.0)

    # Getting smaller
    if size >= min:
        s = size / 3;
        # First square
        drawSierpinski(x - s, y + s, s, min)
        # Second square
        drawSierpinski(x, y + s, s, min)
        # Third square
        drawSierpinski(x + s, y + s, s, min)
        # Fourth square
        drawSierpinski(x + s, y, s, min)
        # Fifth square
        drawSierpinski(x + s, y - s, s, min)
        # Sixth square
        drawSierpinski(x, y - s, s, min)
        # Seventh square
        drawSierpinski(x - s, y - s, s, min)
        # Eighth square
        drawSierpinski(x - s, y, s, min)


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

    window = glfwCreateWindow(800, 800, "Task 3 - Sierpinski's Carpet", None, None)
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
