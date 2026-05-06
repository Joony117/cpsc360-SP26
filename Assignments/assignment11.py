import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 800, 600                                                    # width and height of the screen created

def drawAxes():                                                             # draw x-axis and y-axis
    glLineWidth(3.0)                                                        # specify line size (1.0 default)
    glBegin(GL_LINES)                                                       # replace GL_LINES with GL_LINE_STRIP or GL_LINE_LOOP
    glColor3f(1.0, 0.0, 0.0)                                                # x-axis: red
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(100.0, 0.0, 0.0)                                             # v1
    glColor3f(0.0, 1.0, 0.0)                                                # y-axis: green
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(0.0, 100.0, 0.0)                                             # v1
    glColor3f(0.0, 0.0, 1.0)                                                # z-axis: green
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(0.0, 0.0, 100.0)                                             # v1
    glEnd()

# TODO: Question 1
def draw_cube():
    # TODO: Construct the cube using an Indexed Triangles mesh representation
    # 8 vertices
    vertices = [ 
        [-10.0, -10.0,  10.0],  # v0  front-bottom-left
        [-10.0, -10.0, -10.0],  # v1  back-bottom-left
        [ 10.0, -10.0, -10.0],  # v2  back-bottom-right
        [ 10.0, -10.0,  10.0],  # v3  front-bottom-right
        [-10.0,  10.0, -10.0],  # v4  back-top-left
        [-10.0,  10.0,  10.0],  # v5  front-top-left
        [ 10.0,  10.0,  10.0],  # v6  front-top-right
        [ 10.0,  10.0, -10.0],  # v7  back-top-right

    ]

    # 12 triangles
    triangles = [
        # Front face, BLUE
        [0, 3, 6],
        [0, 6, 5],
        # Back face, BLUE
        [2, 1, 4],
        [2, 4, 7],
        # Left face RED
        [1, 0, 5],
        [1, 5, 4],
        # Right face RED
        [3, 2, 7],
        [3, 7, 6],
        # Top face GREEN 
        [6, 4, 5],
        [4, 6, 7],
        # Bottom face GREEN 
        [0, 1, 2],
        [0, 2, 3],
    ]
    
    # 12 edges
    edges = [  
        # Bottom square
        [0, 1], [1, 2], [2, 3], [3, 0],
        # Top square
        [4, 5], [5, 6], [6, 7], [7, 4],
        # sides
        [0, 5], [1, 4], [2, 7], [3, 6],
    ]
    
    # resotre the colors for all the faces in a list of tuples: [(r, g, b), (), ...]
    colors = [
        (0.0, 0.0, 1.0), (0.0, 0.0, 1.0),  # front  blue
        (0.0, 0.0, 1.0), (0.0, 0.0, 1.0),  # back   blue
        (1.0, 0.0, 0.0), (1.0, 0.0, 0.0),  # left   red
        (1.0, 0.0, 0.0), (1.0, 0.0, 0.0),  # right  red
        (0.0, 1.0, 0.0), (0.0, 1.0, 0.0),  # top    green
        (0.0, 1.0, 0.0), (0.0, 1.0, 0.0),  # bottom green
    ]
    
    # TODO: draw all the 12 triangles using GL_TRIANGLES
    tri_idx = 0
    glBegin(GL_TRIANGLES)
    for triangle in triangles:
        glColor3fv(colors[tri_idx])
        for vertex in triangle:
            glVertex3fv(vertices[vertex])
        tri_idx += 1
    glEnd()
    
    
    # TODO: draw all the 12 edges in white with a line width of 5 using GL_LINES
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
 
    return

# TODO: Question 2
def draw_pyramid():
    # TODO: Construct the pyramid using an Indexed Triangles mesh representation
    # 5 vertices
    vertices = [
        [-10.0,  0.0,  10.0],  # v0, front-left of base
        [-10.0,  0.0, -10.0],  # v1, back-left of base
        [ 10.0,  0.0, -10.0],  # v2, back-right of base
        [ 10.0,  0.0,  10.0],  # v3, front-right of base
        [  0.0, 20.0,   0.0],  # v4, apex
    ]

    # 6 triangles
    triangles = [
        # Bottom face BLUE
        [0, 1, 2],
        [0, 2, 3],
        # Front face YELLOW
        [0, 3, 4],
        # Right face GREEN
        [3, 2, 4],
        # Back face TURQUOISE
        [2, 1, 4],
        # Left face RED
        [1, 0, 4],
    ]

    # 8 edges
    edges = [
        # Base
        [0, 1], [1, 2], [2, 3], [3, 0],
        # Apex edges
        [0, 4], [1, 4], [2, 4], [3, 4],
    ]

    # TODO: draw all the 6 triangles using GL_TRIANGLES
    # resotre the colors for all the faces in a list of tuples: [(r, g, b), (), ...]
    colors = [
        (0.0, 0.0, 1.0),  # bottom triangle  blue
        (0.0, 0.0, 1.0),  # bottom triangle  blue
        (1.0, 1.0, 0.0),  # front yellow
        (0.0, 1.0, 0.0),  # right green
        (0.0, 1.0, 1.0),  # back  turquoise
        (1.0, 0.0, 0.0),  # left  red
    ]



    # TODO: draw all the 8 edges in white with a line width of 5 using GL_LINES
    tri_idx = 0
    glBegin(GL_TRIANGLES)
    for triangle in triangles:
        glColor3fv(colors[tri_idx])
        for vertex in triangle:
            glVertex3fv(vertices[vertex])
        tri_idx += 1  
    glEnd()
 
    # Draw the 8 edges in white with line width 5
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    return

def draw():
    glClearColor(0, 0, 0, 1)                                                # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)                        # clear the buffers initialized in the display mode
    glEnable(GL_CULL_FACE)                                                  # enable front/back face culling
    glCullFace(GL_BACK)                                                     # specify which face NOT drawing (culling)
    
    #TODO: write your code for Q1 inside draw_cube()
    #draw_cube()

    #TODO: write your code for Q2 inside draw_pyramid()
    draw_pyramid()


def main():
    pygame.init()                                                           # initialize a pygame program
    glutInit()                                                              # initialize glut library 

    screen = (width, height)                                                # specify the screen size of the new program window
    display_surface = pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)   # create a display of size 'screen', use double-buffers and OpenGL
    pygame.display.set_caption('CPSC 360 - Jun Yi')                      # set title of the program window

    glEnable(GL_DEPTH_TEST)
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    glOrtho(-40, 40, -30, 30, 10, 80)                                       # specify an orthogonal-projection view volume

    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric + view transf)
    gluLookAt(0, 0, 50, 0, 0, 0, 0, 1, 0)                                   # set camera's eye, look-at, and view-up in the world
    initmodelMatrix = glGetFloat(GL_MODELVIEW_MATRIX)
    while True:
        bResetModelMatrix = False

        # user interface event handling
        for event in pygame.event.get():

            # quit the window
            if event.type == pygame.QUIT:
                pygame.quit()

            # mouse event
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    glRotatef(event.rel[1], 1, 0, 0)
                    glRotatef(event.rel[0], 0, 1, 0)

            # keyboard event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    bResetModelMatrix = True

        # reset the current model-view back to the initial matrix
        if (bResetModelMatrix):
            glLoadMatrixf(initmodelMatrix)
        
        draw()
        drawAxes()

        pygame.display.flip()
        pygame.time.wait(10)

main()