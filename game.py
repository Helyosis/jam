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
        
        player_character = Player(50, 50, self)
        player_character.add(self.all_sprites)

        floor = Floor(x = 0, y = 380, width=800)
        floor.add(self.all_sprites, self.collide_with_player)

        platform = Floor(x = 380, y = 300, width=140)
        platform.add(self.all_sprites, self.collide_with_player)

        enemy = Enemy(400, 250, self)
        enemy.add(self.all_sprites, self.collide_with_player)

        ui = Ui(self.display, self.width ,self.height,499,190,300,400,'Hey salut à tous les amis,|c\'est DavidLaFargePokémon')
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

if __name__ == "__main__":
    pygame.init()

    WIDTH, HEIGHT = 800, 600

    display=pygame.display.set_mode((WIDTH,HEIGHT))
    game = Game(WIDTH, HEIGHT, display)
    game.run()
