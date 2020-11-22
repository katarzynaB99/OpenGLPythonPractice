
# ------------------------------------------------------------
# Class 1 - Task 1
# Generate a triangle with different colors for each vertex
#-------------------------------------------------------------

import sys
from glfw.GLFW import *
from OpenGL.GL import *


def startup():
    glClearColor(0.5, 0.5, 0.5, 1.0)
    update_viewport(None, 800, 800)


def shutdown():
    pass


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    # First vertex (red)
    glColor(1.0, 0.0, 0.0)
    glVertex2f(0.0, 50.0)

    # Second vertex (green)
    glColor(0.0, 1.0, 0.0)
    glVertex2f(-70.0, -40.0)

    # Third vertex (blue)
    glColor(0.0, 0.0, 1.0)
    glVertex2f(70.0, -40.0)

    glEnd()

    glFlush()


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

    window = glfwCreateWindow(800, 800, "Task 1", None, None)
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
