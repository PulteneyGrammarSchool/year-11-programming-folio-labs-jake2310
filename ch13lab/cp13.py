import pygame
import random

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE = (0,0,255)
GREEN = (0,255,0)
touching = False

class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = color
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        global touching
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x < 0:
            self.rect.x = 0
            touching = True
        if self.rect.x > 685:
            self.rect.x = 685
            touching = True
        if self.rect.y < 0:
            self.rect.y = 0
            touching = True
        if self.rect.y > 385:
            self.rect.y = 385
            touching = True


# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

zombie_red = pygame.image.load("zombie_red.png").convert()
zombie_blue = pygame.image.load("zombie_blue.png").convert()
zombie_red = pygame.transform.scale(zombie_red, (20, 15))
zombie_blue = pygame.transform.scale(zombie_blue, (20, 15))


# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
good_sprites = pygame.sprite.Group()
bad_sprites = pygame.sprite.Group()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Score: ' + '0', False, (0, 0, 0))
block_sound = pygame.mixer.Sound("good_block.wav")
block1_sound = pygame.mixer.Sound("bad_block.wav")
block3_sound = pygame.mixer.Sound("bump.wav")
for i in range(50):
    # This represents a block
    block = Block(zombie_blue, 20, 15)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Add the block to the list of objects
    block_list.add(block)
    good_sprites.add(block)

for i in range(50):
    # This represents a block
    block = Block(zombie_red, 20, 15)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Add the block to the list of objects
    block_list.add(block)
    bad_sprites.add(block)

# Create a RED player block
player = Player(100, 100)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
    # Clear the screen
    screen.fill(WHITE)

    all_sprites_list.update()
    # See if the player block has collided with anything.
    if pygame.sprite.spritecollide(player, good_sprites, False):
        pygame.mixer.Sound.play(block_sound)
    if pygame.sprite.spritecollide(player, bad_sprites, False):
        pygame.mixer.Sound.play(block1_sound)
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)


    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)
        textsurface = myfont.render('Score: ' + str(score), False, (0, 0, 0))
    # Draw all the spites
    screen.blit(textsurface,(0,0))
    if touching:
        print('qQQQQQQQQQ')
        pygame.mixer.Sound.play(block3_sound)
    all_sprites_list.draw(screen)
    good_sprites.draw(screen)
    bad_sprites.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    touching = False
    clock.tick(60)

pygame.quit()
