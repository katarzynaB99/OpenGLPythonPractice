
# ------------------------------------------------------------
# Class 1 - Task 2
# Generate a 2D rectangle with given dimensions in the
#   given place of the coordinate system
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

    # Draw rectangle
    draw_rectangle(10.0, -50.0, 80.0, 50.0)

    glFlush()


def draw_rectangle(x, y, a, b):
    # x, y - coordinates of the center of the rectangle
    # a, b - rectangle dimensions

    # First triangle
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)

    glVertex2f(x - a / 2, y + b / 2)
    glVertex2f(x + a / 2, y + b / 2)
    glVertex2f(x + a / 2, y - b / 2)

    glEnd()

    # Second triangle
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)

    glVertex2f(x - a / 2, y + b / 2)
    glVertex2f(x + a / 2, y - b / 2)
    glVertex2f(x - a / 2, y - b / 2)

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

    window = glfwCreateWindow(800, 800, "Task 2", None, None)
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
