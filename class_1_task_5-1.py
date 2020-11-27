# ------------------------------------------------------------
# Class 1 - Task 5
# Generate a different fractal (Koch's Snowflake)
#
# Comment: this is the first attempt at the task,
#          where the Snowflake is generated using
#          triangles.
# -------------------------------------------------------------

import sys
import math
from glfw.GLFW import *
from OpenGL.GL import *

pointArray = []


def startup():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    update_viewport(None, 800, 800)


def shutdown():
    pass


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    draw_koch(0.0, 0.0, 150.0, 2.0)

    glFlush()


def draw_triangle(x, y, size, color):
    height = size * math.sqrt(3) / 2

    b = height / 3
    a = 2 * b

    glColor3f(color, color, color)
    glBegin(GL_TRIANGLES)

    glVertex2f(x - size / 2, y - b)
    glVertex2f(x, y + a)
    glVertex2f(x + size / 2, y - b)

    glEnd()


def draw_triangle_inv(x, y, size, color):
    height = size * math.sqrt(3) / 2

    b = height / 3
    a = 2 * b

    glColor3f(color, color, color)
    glBegin(GL_TRIANGLES)

    glVertex2f(x - size / 2, y + b)
    glVertex2f(x + size / 2, y + b)
    glVertex2f(x, y - a)

    glEnd()


def draw_koch(x, y, size, outline):
    draw_koch_star(x, y, size, 1.0)
    # drawKochStar(x, y, size - outline, 0.0)


def draw_koch_star(x, y, size, color):
    draw_triangle(x, y, size, color)
    draw_triangle_inv(x, y, size, color)

    # 6 little stars, size/3
    if size >= 1.0:
        s = size / 3
        h = s * math.sqrt(3) / 2
        a = 2 * h / 3

        # 1
        draw_koch_star(x, y + 2 * a, s, color)
        # 2
        draw_koch_star(x + s, y + a, s, color)
        # 3
        draw_koch_star(x + s, y - a, s, color)
        # 4
        draw_koch_star(x, y - 2 * a, s, color)
        # 5
        draw_koch_star(x - s, y - a, s, color)
        # 6
        draw_koch_star(x - s, y + a, s, color)


def draw_side(x, y, size, outline):
    height = size * math.sqrt(3) / 2

    b = height / 3
    a = 2 * b

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)

    glVertex2f(x - size / 2, y - b)
    glVertex2f(x, y + a)
    glVertex2f(x + size / 2, y - b)

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

    window = glfwCreateWindow(800, 800, "Task 5 - Koch's Snowflake", None, None)
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
