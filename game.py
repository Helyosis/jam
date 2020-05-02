import pygame

from player import Player
from enemy import Enemy
from block import Block
from ui import Ui

class Game:
    def __init__(self, width, height, display):
        self.width = width
        self.height = height
        self.display = display

        self.slow_time = False

        self.all_sprites = pygame.sprite.Group()
        self.all_game_objects = pygame.sprite.Group()
        self.background = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.characters = pygame.sprite.Group()
        self.foreground = pygame.sprite.Group()

        self.layers_list = [self.all_sprites, self.background, self.platforms, self.characters, self.foreground]

        self.collide_with_player = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        
        self.player_character = Player(50, 50, self)
        self.player_character.add(self.all_sprites, self.all_game_objects, self.characters)

        floor = Block(x = 0, y = 380, width=800)
        floor.add(self.all_sprites, self.collide_with_player, self.platforms)

        platform = Block(x = 380, y = 300, width=140)
        platform.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)

        enemy = Enemy(400, 250, self, platform)
        enemy.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.characters)

        texte = "Je crois que les filles m'aiment bien parceque je suis un peu mystérieux comme Light Yagami, je suis toujours tout seul, aux récrées je m’assoie sur un banc avec ma capuche et la tête baissé et quand quelque passe à coté de moi je chuchote des truc genre okamari no suzoki, ça ne veut rien dire mais ça fait mystique, les gens sont intrigués."
        self.ui = Ui(self.display, self.width ,self.height,499,190,300,400, texte)
        self.ui.add(self.all_sprites, self.foreground)
    
    def scroll(self, dx = -1, dy = 0):
        """
        Move all sprites belonging to self.all_game_objects Group by applying their function force_move(dx)
        dx: int. Number of pixel to move to the right (negative dx = moving to the left)
        """
        for sprite in self.all_game_objects.sprites():
            sprite.force_move(dx = dx, dy = dy)

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

            #Draw sprites, in respect of their layers
            for layer in self.layers_list:
                layer.draw(self.display)

            #Refresh display and set FPS to 60
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    pygame.init()

    WIDTH, HEIGHT = 800, 600

    display=pygame.display.set_mode((WIDTH,HEIGHT))
    game = Game(WIDTH, HEIGHT, display)
    game.run()
