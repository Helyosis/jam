import pygame
pygame.init()

from player import Player


launched = True
width, height = 800, 600

screen = pygame.display.set_mode((width, height))

all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

player = Player(50, 50)
all_sprites.add(player)

while launched:
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                launched=False

    all_sprites.update()

    #Draw background
    screen.fill((0,255,0))

    #Draw sprites
    all_sprites.draw(screen)

    #Refresh display and set FPS to 60
    pygame.display.flip()
    clock.tick(60)