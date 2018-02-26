# Import a library of functions called 'pygame'
import pygame
import random
import math


# Initialize the game engine
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# Set the height and width of the screen
SIZE = [400, 400]
x1 = 0
y1 = 0
x_velocity = 10
y_velocity = 9
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")
clock = pygame.time.Clock()
num = 0
state1 = False
t = 1


places_ive_been = []

# Loop until the user clicks the close button.
done = False
while not done:

    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)
    x1 = x1 + x_velocity
    if x1 > 400:
      x_velocity = x_velocity * -1
    if x1 < 0:
      x_velocity = x_velocity * -1
    print(x1)
    y1 = y1 + y_velocity
    if y1 < -400:
        state1 = False
    if y1 > 400:
      y_velocity = y_velocity * -1
      state1 = True
    if y1 < 0:
      y_velocity = y_velocity * -1
      state1 = True
    print(y1)



    places_ive_been.append([(x1+10), (y1+10)])

#    for place in places_ive_been:
#        print(place)
#        pygame.draw.ellipse(screen, WHITE, [place[0], place[1],4,4], 2)
    if len(places_ive_been) > 2:
        pygame.draw.lines(screen, WHITE, False, places_ive_been, 1)

    #print(places_ive_been)

    pygame.draw.rect(screen, WHITE, [x1, y1, 20, 20], 3)

    t = t + 0.5

    circle_x = 100*math.sin(t) + 200
    circle_y = 100*math.cos(t) + 200
    pygame.draw.rect(screen, WHITE, [circle_x, circle_y, 20, 20], 3)



    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
