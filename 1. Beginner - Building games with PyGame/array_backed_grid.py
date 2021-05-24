"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

# This sets the width and height of each grid location
width  = 20
height = 20

# This sets the margin between each cell
margin = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0) # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

# Initialize pygame
pygame.init()

# Set the height and width of the screen
size = [255, 255]
screen = pygame.display.set_mode(size)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while done == False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            # Set that location to zero
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(margin+width)*column+margin,
                              (margin+height)*row+margin,
                              width,
                              height])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

