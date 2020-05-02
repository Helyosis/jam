import pygame

from player import Player
from enemy import Enemy
from floor import Floor
from ui import Ui

class Game:
    def __init__(self, width, height, display):
        self.width = width
        self.height = height
        self.display = display

        self.all_sprites = pygame.sprite.Group()
        self.collide_with_player = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        
        player_character = Player(50, 50, self.collide_with_player)
        player_character.add(self.all_sprites)

        floor = Floor(x = 0, y = 450, width=800)
        floor.add(self.all_sprites, self.collide_with_player)

        platform = Floor(x = 300, y = 500, width = 120)
        platform.add(self.all_sprites, self.collide_with_player)

        scientist = Enemy(x = 320, y = 500)
        scientist.add(self.all_sprites, self.collide_with_player)

        ui = Ui(self.display, self.width ,self.height,499,190,300,400,'hello  ceci est un super |retour à la ligneeeeee! |cest pas mal mais bon |1 |2 |3 |4 |5')
        ui.add(self.all_sprites)
    
    def run(self):
        game_launched = True
        while game_launched:
            #if pygame.event.get(pygame.MOUSEMOTION):
            #print(pygame.mouse.get_pos())
            if pygame.event.get(pygame.QUIT):
                game_launched=False

            #Game logic
            self.all_sprites.update()

            #Draw background
            self.display.fill((0,255,0))

            #Draw sprites
            self.all_sprites.draw(self.display)

            #Refresh display and set FPS to 60
            pygame.display.flip()
            self.clock.tick(60)