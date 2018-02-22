
import pygame
import random


pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (128,0,0)
BROWN = (222,184,135)
YELLOW = (255,255,0)
GREEN2 = (34,139,34)

PI = 3.141592653
YOff = 100

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Professor Craven's Cool Game")

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
            print(pygame.mouse.get_pos()
        #elif event.type == pygame.KEYDOWN:
        #    print(event.key)
        #    if event.key == 274:
        #        print('Down')
        #        YOff = YOff + 1
        #    if event.key == 273:
        #        print('Up')
        #        YOff = YOff - 1






    screen.fill(GREEN2)
    pygame.draw.rect(screen, (139,69,19), [161, 334, 20, 90])
    pygame.draw.ellipse(screen, GREEN, [129, 295,80,80])
    pygame.draw.rect(screen, RED, [0, YOff, 400, 100])
    pygame.draw.rect(screen, BROWN, [80, 150, 40, 50])
    pygame.draw.rect(screen, BLACK, [241, 200, 120, 400])
    pygame.draw.rect(screen, BLACK, [78, 200, 40, 250])
    pygame.draw.rect(screen, BLACK, [78, 410, 250, 40])
    pygame.draw.polygon(screen, BLUE, [[200, 0], [400, 100], [400, 0]])
    pygame.draw.polygon(screen, BLUE, [[0, 0], [0, 100], [200, 0]])
    pygame.draw.polygon(screen, RED, [[400, 100], [200, 0], [0, 100]])
    pygame.draw.ellipse(screen, BLACK, [113, 178,4,4], 2)
    pygame.draw.line(screen, BLACK, [0, 100], [400, 100], 2)
    pygame.draw.ellipse(screen, YELLOW, [340, 13,40,40])
    random.seed(3)
    for x_offset in range(0, 400, 5):
        if x_offset > 117 or x_offset < 79:
            pygame.draw.line(screen,GREEN,[0+x_offset+random.randint(-10,10),190],[0+x_offset,220],2)
    random.seed(4)
    for x_offset in range(0, 400, 5):
        if x_offset > 117 or x_offset < 79:
            pygame.draw.line(screen,GREEN,[0+x_offset+random.randint(-10,10),200],[0+x_offset,220],2)
    random.seed(5)
    for x_offset in range(0, 400, 5):
        if x_offset > 117 or x_offset < 79:
            pygame.draw.line(screen,GREEN,[0+x_offset+random.randint(-10,10),200],[0+x_offset,220],2)


    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()
