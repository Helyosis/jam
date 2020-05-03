import pygame

from player import Player
from enemy import Enemy
from block import Block
from ui import Ui
from bullet import Bullet
from laser import LaserShooter
class Game:
    #ralentire la music #TODO
    
    def __init__(self, width, height, display):
        self.width = width
        self.height = height
        self.display = display

        self.SCROLL_X = 400
        self.SCROLL_Y = 200
        self.x = self.y = 0

        self.MAX_X = 2500

        self.slow_time = -1

        self.all_sprites = pygame.sprite.Group()
        self.all_game_objects = pygame.sprite.Group()
        self.background = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.characters = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.foreground = pygame.sprite.Group()

        self.layers_list = [self.all_sprites, self.background, self.projectiles, self.platforms, self.characters, self.foreground]

        self.collide_with_player = pygame.sprite.Group()

        self.clock = pygame.time.Clock()
        
        self.player_character = Player(50, 50, self)
        self.player_character.add(self.all_sprites, self.all_game_objects, self.characters)

        platform = Block(x = 380, y = 300, width=140, game = self)
        platform.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)

        path = [(0, 1) for _ in range(400, 500)] + [(0, -1) for y in range(500, 400, -1)]
        moving_platform = Block(x = 1000, y = 300, width = 150, path = path, game = self, texture = (0, 0, 0))
        moving_platform.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)

        platform1 = Block(x = 1350, y = 100, game=self)
        platform1.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)
        platform1 = Block(x = 1300, y = 200, game=self)
        platform1.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)
        platform1 = Block(x = 1250, y = 300, game=self)
        platform1.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)
        platform1 = Block(x = 1200, y = 360, game=self)
        platform1.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)

        enemy = Enemy(400, 250, self, platform)
        enemy.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.characters)

        laser_shooter = LaserShooter(1400, 360, self, "UP", 10)
        laser_shooter.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)

        #texte = "Je crois que les filles m'aiment bien parceque je suis un peu mystérieux comme Light Yagami, je suis toujours tout seul, aux récrées je m’assoie sur un banc avec ma capuche et la tête baissé et quand quelque passe à coté de moi je chuchote des truc genre okamari no suzoki, ça ne veut rien dire mais ça fait mystique, les gens sont intrigués."
        texte = "Bonjour.|Bonne chance"
        self.ui = Ui(self.display, self.width ,self.height,499,190,300,400, texte, self)
        self.ui.add(self.all_sprites, self.foreground)
    
    def initialize_level(self):
        floor = Block(x = 0, y = 380, width=self.MAX_X, game = self)
        floor.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)

    def scroll(self, dx = -1, dy = 0):
        """
        Move all sprites belonging to self.all_game_objects Group by applying their function force_move(dx)
        dx: int. Number of pixel to move to the right (negative dx = moving to the left)
        """

        if self.x + dx <= 0 and self.y - dy <= 0:
            self.x += dx
            self.y -= dy

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
            self.all_sprites.draw(self.display)

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
