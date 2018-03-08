
import pygame
import random
def shape1(a,b):
    pygame.draw.polygon(screen, BLACK, [[0+a, 30+b], [15+a, 0+b], [30+a, 30+b]])
def shape2(c,d):
    pygame.draw.rect(screen, BLACK, [0, 200, 75, 10])
def shape3(e):
    pygame.draw.line(screen, BLACK, [e,460],[e,500],3)
def lives(current_lives):
    for i in range(current_lives):
        pygame.draw.rect(screen, BLACK, [400 - (40*(i+1)), 10, 20,20])


pygame.init()

print('no')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (128,0,0)
BROWN = (222,184,135)
YELLOW = (255,255,0)
GREEN2 = (34,139,34)

PI = 3.141592653
YOff = 500
XOff = 0
Xvel = 0
Yvel = 0

bullets = []
life = 3

size = (430, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Professor Craven's Cool Game")
up = False
down = False

done = False
clock = pygame.time.Clock()
tick = 0


while not done:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
            print(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            print(event.key, 'this is the key')
            if event.key == 32:
                print('done')
                down = True
            if event.key == 27:
                done = True
        elif event.type == pygame.KEYUP:
            if event.key == 32:
                up = True
                print('done again')

    key = pygame.key.get_pressed()

    if key[275]:
        print('right key pressed')
        XOff = XOff + 10
    if key[276]:
        print('left key pressed')
        XOff = XOff - 10


    if XOff > 400:
        Xvel = 0
        XOff = 400
    if XOff < 0:
        Xvel = 0
        XOff = 0
    XOff = XOff + Xvel
    YOff = YOff + Yvel
    print(XOff)
    print(Xvel)

    if up and down == True:
        print('fire')
        up = False
        down = False
        print('reset')
        bullets.append([XOff+15, 500])

    for bullet in bullets:
        pygame.draw.ellipse(screen, BLACK, [bullet[0], bullet[1],5,5])
        bullet[1] = bullet[1] - 10

    bullets_to_delete = []
    current_mos_pos = pygame.mouse.get_pos()

    this_shape = pygame.Rect(current_mos_pos[0], 200, 75, 10)
    for point in bullets:
        if this_shape.collidepoint(point) == True:
            bullets_to_delete.append(point)
    for post in bullets:
        print(post)
        if post[1] < 0:
            life = life - 1
            bullets_to_delete.append(post)
    for item_to_remove in bullets_to_delete:
        bullets.remove(item_to_remove)
    if life == 0:
        done = True

    print(pygame.mouse.get_pos())
    pygame.draw.rect(screen, BLACK, [this_shape.x, this_shape.y, this_shape.width, this_shape.height])
    shape1(XOff,YOff)
    lives(life)
    pygame.display.flip()

    print(tick)
    clock.tick(60)

pygame.quit()
