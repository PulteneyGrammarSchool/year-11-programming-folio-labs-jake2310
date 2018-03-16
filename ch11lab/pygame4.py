import pygame
import random
import math
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.font.init()

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 800])

# This sets the name of the window
pygame.display.set_caption('Dont get bit!')
zombies_up = []
zombies_down = []
zombies_left = []
zombies_right = []
clock = pygame.time.Clock()

# Before the loop, load the sounds:
click_sound = pygame.mixer.Sound("laser5.ogg")
current_punch = pygame.Rect(1000,1000,1,1)
# Set positions of graphics
to_delete_up = []
to_delete_down = []
to_delete_left = []
to_delete_right = []
time_elaspsed_since_last_action = 0
player_direction = 'east'
# Load and set up graphics.
zombie_image = pygame.image.load("zombie.png").convert()
player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(BLACK)
og_player_image = pygame.transform.scale(player_image, (80, 80))
og_zombie_image = pygame.transform.scale(zombie_image, (40, 40))
og_zombie_image.set_colorkey(BLACK)
done = False
player_image = pygame.transform.rotate(og_player_image, 0)
zombie_1 = pygame.transform.rotate(og_zombie_image, 180)
zombie_2 = pygame.transform.rotate(og_zombie_image, 90)
zombie_3 = pygame.transform.rotate(og_zombie_image, 270)
zombies_up = []
punch = False
kill_counter = 0
spawn_per = 0
myfont = pygame.font.SysFont('Comic Sans MS', 30)
myfont2 = pygame.font.SysFont('Comic Sans MS', 72)
spawn = False
start = False
dead = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
        elif event.type == pygame.KEYDOWN:
            #print(event.key, 'this is the key')
            if event.key == 27:
                done = True
            #if event.key == 119:
                #zombies_up.append([random.randint(0,600), 800])
                #zombies_down.append([random.randint(0,600), 0])
                #zombies_left.append([800, random.randint(0,600)])
                #zombies_right.append([0, random.randint(0,600)])
            elif event.key == 32:
                punch = True
    screen.fill(WHITE)
    spawn_per = round(kill_counter/50,0)
    if spawn_per == 0.0:
        spawn_per = 1
    print(spawn_per)
    print(pygame.time.get_ticks()%1000)
    if pygame.time.get_ticks()%1000 > 900:
        spawn = True
    if spawn:
        for i in range(int(spawn_per)):
            x_for_zom = random.randint(0,600)
            x_for_zom2 = random.randint(0,600)
            side = random.randint(1,4)
            if side == 1:
                zombies_down.append([x_for_zom, 0])
            if side == 2:
                zombies_up.append([x_for_zom, 800])
            if side == 3:
                zombies_left.append([800, x_for_zom2])
            if side == 4:
                zombies_right.append([0, x_for_zom2])
        print('Spawming')
    spawn = False




    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    key = pygame.key.get_pressed()
    if key[275]:
        #print('right key pressed')
        player_image = pygame.transform.rotate(og_player_image, 0)
        player_direction = 'east'
    if key[276]:
        #print('left key pressed')
        player_image = pygame.transform.rotate(og_player_image, 180)
        player_direction = 'west'
    if key[273]:
        #print('up key is pressed')
        player_image = pygame.transform.rotate(og_player_image, 90)
        player_direction = 'north'
    if key[274]:
        #print('down key is pressed')
        player_image = pygame.transform.rotate(og_player_image, 270)
        player_direction = 'south'

    for abcd in zombies_up:
        zx = abcd[0]
        zy = abcd[1]
        dx = x - 15 - abcd[0]
        dy = y - 15 - abcd[1]
        d = math.sqrt((dx**2)+(dy**2))
        dx = dx/d
        dy = dy/d
        zx = zx+(1*dx)
        zy = zy+(1*dy)
        abcd[0] = zx
        abcd[1] = zy
        screen.blit(og_zombie_image, [zx,zy])
    for abcd in zombies_down:
        zx = abcd[0]
        zy = abcd[1]
        dx = x - abcd[0]
        dy = y - abcd[1]
        d = math.sqrt((dx**2)+(dy**2))
        dx = dx/d
        dy = dy/d
        zx = zx+(1*dx)
        zy = zy+(1*dy)
        abcd[0] = zx
        abcd[1] = zy
        screen.blit(zombie_1, [zx,zy])
    for abcd in zombies_left:
        zx = abcd[0]
        zy = abcd[1]
        dx = x - abcd[0]
        dy = y - abcd[1]
        d = math.sqrt((dx**2)+(dy**2))
        dx = dx/d
        dy = dy/d
        zx = zx+(1*dx)
        zy = zy+(1*dy)
        abcd[0] = zx
        abcd[1] = zy
        screen.blit(zombie_2, [zx,zy])
    for abcd in zombies_right:
        zx = abcd[0]
        zy = abcd[1]
        dx = x - abcd[0]
        dy = y - abcd[1]
        d = math.sqrt((dx**2)+(dy**2))
        dx = dx/d
        dy = dy/d
        zx = zx+(1*dx)
        zy = zy+(1*dy)
        abcd[0] = zx
        abcd[1] = zy
        screen.blit(zombie_3, [zx,zy])


    screen.blit(player_image, [x-40, y-40])
    if punch == True:
        if player_direction == 'east':
            pygame.draw.rect(screen, BLACK, [x, y-40,80,80],3)
            current_punch = pygame.Rect(x, y-40,80,80)
        if player_direction == 'west':
            pygame.draw.rect(screen, BLACK, [x-80, y-40,80,80],3)
            current_punch = pygame.Rect(x-80, y-40,80,80)
        if player_direction == "north":
            pygame.draw.rect(screen, BLACK, [x-40, y-80,80,80],3)
            current_punch = pygame.Rect(x-40, y-80,80,80)
        if player_direction ==  'south':
            pygame.draw.rect(screen, BLACK, [x-40, y,80,80],3)
            current_punch = pygame.Rect(x-40, y,80,80)
    punch = False
    for point in zombies_up:
        if current_punch.collidepoint(point) == True:
            to_delete_up.append(point)
    for zom_to_delete in to_delete_up:
        times_though = 1
        times_though = times_though + 1
        zombies_up.remove(zom_to_delete)
        to_delete_up.remove(zom_to_delete)
        kill_counter = kill_counter + 1

    for point in zombies_down:
        if current_punch.collidepoint(point) == True:
            to_delete_down.append(point)
    for zom_to_delete in to_delete_down:
        zombies_down.remove(zom_to_delete)
        to_delete_down.remove(zom_to_delete)
        kill_counter = kill_counter + 1

    for point in zombies_left:
        if current_punch.collidepoint(point) == True:
            to_delete_left.append(point)
    for zom_to_delete in to_delete_left:
        zombies_left.remove(zom_to_delete)
        to_delete_left.remove(zom_to_delete)
        kill_counter = kill_counter + 1

    for point in zombies_right:
        if current_punch.collidepoint(point) == True:
           to_delete_right.append(point)
    for zom_to_delete in to_delete_right:
        zombies_right.remove(zom_to_delete)
        to_delete_right.remove(zom_to_delete)
        kill_counter = kill_counter + 1

    current_punch = pygame.Rect(1000,1000,1,1)
    textsurface = myfont.render('Kills: ' + str(kill_counter), False, (0, 0, 0))
    textsurface1 = myfont.render('Zombies per second: ' + str(spawn_per), False, (0, 0, 0))
    screen.blit(textsurface,(0,0))
    screen.blit(textsurface1,(0,80))
    player_rect = pygame.Rect(x,y,40,40)
    for point in zombies_up:
        if player_rect.collidepoint(point) == True:
            #done = True
            dead = True
    for point in zombies_down:
        if player_rect.collidepoint(point) == True:
            #done = True
            dead = True
    for point in zombies_left:
        if player_rect.collidepoint(point) == True:
            #done = True
            dead = True
    for point in zombies_right:
        if player_rect.collidepoint(point) == True:
            #done = True
            dead = True
    if dead == True:
        textsurface2 = myfont2.render("DEAD", False, (255, 0, 0))
        screen.blit(textsurface2,(300,300))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
