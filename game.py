import pygame

from player import Player
from enemy import Enemy
from block import Block
from ui import Ui
from bullet import Bullet
from laser import Laser
import threading, time
from laser import LaserShooter
from coin import Coin
class Game:
    #ralentire la music #TODO
    
    def __init__(self, width, height, display):
        self.width = width
        self.height = height
        self.display = display

        self.SCROLL_X = 400
        self.SCROLL_Y = 200
        self.x = self.y = 0

        self.FLOOR_Y_LEVEL = 380
        self.MAX_X = 5000
        self.MAX_Y = 5000

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
        
        self.player_character = Player(50, self.FLOOR_Y_LEVEL - 50, self)
        self.player_character.add(self.all_sprites, self.all_game_objects, self.characters)

        self.initialize_level()

        #texte = "Je crois que les filles m'aiment bien parceque je suis un peu mystérieux comme Light Yagami, je suis toujours tout seul, aux récrées je m’assoie sur un banc avec ma capuche et la tête baissé et quand quelque passe à coté de moi je chuchote des truc genre okamari no suzoki, ça ne veut rien dire mais ça fait mystique, les gens sont intrigués."
        texte = "Bonjour.|Bonne chance"
        self.ui = Ui(self.display, self.width ,self.height,499,190,300,400, texte, self)
        self.ui.add(self.all_sprites, self.foreground)

        self.game_song_slow= pygame.mixer.Sound("assets/music1.wav")
        self.game_song= pygame.mixer.Sound("assets/music0.wav")
        self.music()
        self.score = 0


    def initialize_level(self):
        left_border = Block(x = -20, y = -3000, height = 3000 + self.FLOOR_Y_LEVEL, game =self)
        left_border.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)
        right_border = Block(x = self.MAX_X, y = 3000, height = 3000, game =self)
        right_border.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)
        floor = Block(x = 0, y = self.FLOOR_Y_LEVEL, width=self.MAX_X, game = self)
        floor.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)
        roof = Block(x = 0, y = 3000, width = self.MAX_X, game =self)
        roof.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)

        """
        path = [(0, 1) for _ in range(400, 500)] + [(0, -1) for y in range(500, 400, -1)]
        moving_platform = Block(x = 1000, y = 300, width = 150, path = path, game = self, texture = (0, 0, 0))
        moving_platform.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)

        enemy = Enemy(400, 250, self, platform)
        enemy.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.characters)

        laser_shooter = LaserShooter(1400, 360, self, "RIGHT", 10)
        laser_shooter.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)

        fake_block = Block(x = 1000, y = -10, game = self, texture=(255,255,255, 100))
        fake_block.add(self.all_sprites, self.all_game_objects, self.platforms)

        path = [(1, 0) for _ in range(100)] + [(-1, 0) for i in range(100)]
        moving_platform = Block(x = 1000, y = 100, width = 150, path = path, game = self, texture = (0, 0, 0))
        moving_platform.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.platforms)
        """

        #1
        self.add_block_wrapper(0, 200, width = 100)
        self.add_enemy_wrapper(50, 250, aiming_time = 5)
        self.add_coin_wrapper(150, 175)

        #2
        self.add_block_wrapper(900, 150, 80, 150-71)
        self.add_block_wrapper(900, 71, width = 80, height = 71, fake = True)
        self.add_block_wrapper(1000, 250, 80, 250-71)
        self.add_block_wrapper(1000, 71, 80, 71, fake = True)
        self.add_block_wrapper(1100, 350, 80, 350-71)
        self.add_block_wrapper(1100, 71, 80, 71, fake = True)
        self.add_block_wrapper(1200, 450, 80, 450-71)
        self.add_block_wrapper(1200, 71, 80, 71, fake = True)
        self.add_block_wrapper(1300, 600, 80, 600-71)
        self.add_block_wrapper(1300, 71, 80, 71, fake = True)

        #2.5
        self.add_block_wrapper(1300, 600, 900, 40)
        self.add_block_wrapper(1300 + 900, 600, 100, 40, fake = True)
        self.add_coin_wrapper()

        #3
        self.add_block_wrapper(2300, 600, 80, 600-71)
        self.add_block_wrapper(2300, 71,  80, 71, fake = True)
        self.add_block_wrapper(2400, 450, 80, 450-71)
        self.add_block_wrapper(2400, 71, 80, 71, fake = True)
        self.add_block_wrapper(2500, 350, 80, 350-71)
        self.add_block_wrapper(2500, 71, 80, 71, fake = True)
        self.add_block_wrapper(2600, 250, 80, 250-71)
        self.add_block_wrapper(2600, 71, 80, 71, fake = True)
        self.add_block_wrapper(2700, 150, 80, 150-71)
        self.add_block_wrapper(2700, 71, 80, 71, fake = True)


        

    def add_block_wrapper(self, x, y, width = 20, height = 20, texture = (255, 255, 255), path = (), fake = False):
        platform = Block(x = x, y = self.FLOOR_Y_LEVEL - y, width=width, height = height, game = self, texture=texture, path = path)
        platform.add(self.all_sprites, self.all_game_objects, self.platforms)
        if not fake:
            platform.add(self.collide_with_player)

    def add_enemy_wrapper(self, x, y, aiming_time = 2):
        enemy = Enemy(x=x, y=self.FLOOR_Y_LEVEL - y, game=self, aiming_time=aiming_time*60)
        enemy.add(self.all_sprites, self.all_game_objects, self.collide_with_player, self.characters)

    def add_coin_wrapper(self, x, y):
        coin = Coin(x = x,y = self.FLOOR_Y_LEVEL - y, game = self)
        coin.add(self.all_sprites, self.all_game_objects, self.projectiles)

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

    def music(self):
        pos=0
        if self.slow_time<=0:
            pos=pygame.mixer.music.get_pos()
            self.game_song.play(-1,0,1000).set_volume(0.3)#,pos,2#nb rep, tmpmax,fondue 0->100s .set_volume(0.5)
        else:
            #pos=-1*pygame.mixer.music.get_pos()
            self.game_song.stop()
            self.game_song_slow.play(0,0,500)#0,int(pos*1.5),0
            time_thread = threading.Thread(target=self.slow_music, args=(5,))
            time_thread.start()
            
    def slow_music(self,tmp):
        time.sleep(tmp)
        #pos=pygame.mixer.music.get_pos()
        self.game_song_slow.stop()
        self.game_song.play(-1,0,1000).set_volume(0.3)#int(pos/1.5),2

if __name__ == "__main__":
    pygame.init()

    WIDTH, HEIGHT = 800, 600

    display=pygame.display.set_mode((WIDTH,HEIGHT))
    game = Game(WIDTH, HEIGHT, display)
    game.run()
