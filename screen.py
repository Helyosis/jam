import pygame
pygame.init()

from player import Player
from floor import Floor


launched = True
width, height = 1000, 800

screen = pygame.display.set_mode((width, height))

all_sprites = pygame.sprite.Group()
collide_with_player = pygame.sprite.Group()
clock = pygame.time.Clock()

player_character = Player(50, 50, collide_with_player)
all_sprites.add(player_character)

floor = Floor(x = 0, y = 300)
all_sprites.add(floor)
collide_with_player.add(floor)

while launched:
    if pygame.event.get(pygame.QUIT):
        launched=False

    #Game logic
    all_sprites.update()

    #Draw background
    screen.fill((0,255,0))

    #Draw sprites
    all_sprites.draw(screen)

    #Refresh display and set FPS to 60
    pygame.display.flip()
    clock.tick(60)

pygame.quit()