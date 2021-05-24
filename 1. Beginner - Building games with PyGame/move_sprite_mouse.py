# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

import pygame

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
blue     = (  50,  50, 255)
green    = (   0, 255,   0)
dkgreen  = (   0, 100,   0)
red      = ( 255,   0,   0)

# This class represents the ball        
# It derives from the "Sprite" class in Pygame
class Ball(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__() 

        # Variables to hold the height and width of the block
        width = 20
        height = 15

        # Create an image of the ball, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill((black))

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    # Update the position of the ball
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
        
        # Fetch the x and y out of the list, just like we'd fetch letters out of a string.
        # NOTE: If you want to keep the mouse at the bottom of the screen, just set y = 380,
        # and not update it with the mouse position stored in pos[1]
        x=pos[0]
        y=pos[1]

        # Set the attribute for the top left corner where this object is located
        self.rect.x=x
        self.rect.y=y

pygame.init()

# Set the height and width of the screen
size = [700,500]
screen = pygame.display.set_mode(size)

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# This is a list of 'sprites.' Each ball in the program (there is only 1) is
# added to this list. The list is managed by a class called 'Group.'
balls = pygame.sprite.Group()

# This represents the ball controlled by the player
ball = Ball()

# Add the ball to the list of player-controlled objects
balls.add(ball)

# -------- Main Program Loop -----------
while done == False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # Clear the screen
    screen.fill(white)

    # Update the position of the ball (using the mouse) and draw the ball
    ball.update()
    balls.draw(screen)

    # Limit to 20 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
