import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define a simple voxel (cube) for rendering
def draw_voxel(x, y, z, size=1):
    vertices = (
        (x - size, y - size, z - size), (x + size, y - size, z - size),
        (x + size, y + size, z - size), (x - size, y + size, z - size),
        (x - size, y - size, z + size), (x + size, y - size, z + size),
        (x + size, y + size, z + size), (x - size, y + size, z + size)
    )
    edges = (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    )

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Main function to setup OpenGL and run the main loop
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # Draw a simple voxel grid
        for x in range(-5, 6, 2):
            for y in range(-5, 6, 2):
                for z in range(-5, 6, 2):
                    draw_voxel(x, y, z)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
## FT LABS 20XX [C ]
