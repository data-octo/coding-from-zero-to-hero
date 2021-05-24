""" 
 Show how to do a radar sweep.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""
# Import a library of functions called 'pygame'
import pygame
import math

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
black = [  0,   0,   0]
white = [255, 255, 255]
green = [  0, 255,   0]

# Set the height and width of the screen
size = [400, 400]
screen = pygame.display.set_mode(size)

my_clock = pygame.time.Clock()

#Loop until the user clicks the close button.
done = False

angle = 0

while done == False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(white)

    # Dimensions of radar sweep
    # Start with the top left at 20,20
    # Width/height of 250
    box_dimensions = [20, 20, 250, 250]

    # Draw the outline of a circle to 'sweep' the line around
    pygame.draw.ellipse(screen, green, box_dimensions, 2)

    # Draw a black box around the circle
    pygame.draw.rect(screen, black, box_dimensions, 2)

    # Calculate the x,y for the end point of our 'sweep' based on
    # the current angle
    x = 125 * math.sin(angle) + 145
    y = 125 * math.cos(angle) + 145

    # Draw the line from the center at 145, 145 to the calculated
    # end spot
    pygame.draw.line(screen, green, [145, 145], [x, y], 2)

    # Increase the angle by 0.05 radians
    angle = angle + .05

    # If we have done a full sweep, reset the angle to 0
    pi = 3.141592653
    if angle > 2 * pi:
        angle = angle - 2 * pi

    # Flip the display, wait out the clock tick
    pygame.display.flip()
    my_clock.tick(20)    

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()
