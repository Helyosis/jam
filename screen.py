import pygame
from pygame.locals import *
import sys

from button import Button 
from player import Player
from floor import Floor
from ui import Ui
from enemy import Enemy

class Screen(object):

    def __init__(self, width, height):
        #------------------
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Jeu_trop_bien")
        self.width=width
        self.height=height
        self.display=pygame.display.set_mode((self.width,self.height))
        #------------------
        self.game_launched=False
        self.menu_launched=True
        self.menu()
        self.game_0()
        #-----------------
    #-----------------------------------------------------------
    def menu(self):
        mouse_pos=pygame.mouse.get_pos()
        background = pygame.image.load("assets/menu0.png")
        background = pygame.transform.scale(background, (self.width, self.height))
        background.convert()
        self.display.blit(background, (0,0))
        print('requete d\'un super boutton')
        super_boutton=Button(self.display,400,300,100,60,'Play',mouse_pos,'assets/bouton.png')#200/self.width,200/self.height
        menu_song= pygame.mixer.Sound("assets/music0.wav")
        menu_song.play()#nb rep, tmpmax,fondue 0->100s .set_volume(0.5)
        while self.menu_launched:
            for event in pygame.event.get():
                mouse_pos=pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if super_boutton.clic(mouse_pos):
                        self.menu_launched=False
                        #menu_song.stop()
                        self.game_launched=True
                        
                if event.type == pygame.MOUSEMOTION:
                    if super_boutton.clic(mouse_pos):
                        Button(self.display,400,300,100,60,'Play',mouse_pos,'assets/bouton1.png')
                    else:
                        Button(self.display,400,300,100,60,'Play',mouse_pos,'assets/bouton.png')

                if event.type == pygame.QUIT:
                    self.menu_launched = False
                    pygame.quit()
                pygame.display.flip()
#------------------------------------------------------------
    def game_0(self):
        all_sprites = pygame.sprite.Group()
        collide_with_player = pygame.sprite.Group()
        clock = pygame.time.Clock()
        
        player_character = Player(50, 50, collide_with_player)
        all_sprites.add(player_character)

        floor = Floor(x = 0, y = 400, width = 800)
        all_sprites.add(floor)
        collide_with_player.add(floor)

        scientist = Enemy(600, 230)
        all_sprites.add(scientist)
        collide_with_player.add(scientist)

        platform = Floor(x = 600, y= 300, width = 100, color=(255,255,0))
        all_sprites.add(platform)
        collide_with_player.add(platform)

        ui = Ui(self.width,self.height)
        all_sprites.add(ui)
        
        #-----------------
        while self.game_launched:
            if pygame.event.get(pygame.QUIT):
                self.game_launched=False

            #Game logic
            all_sprites.update()

            #Draw background
            self.display.fill((0,255,0))

            #Draw sprites
            all_sprites.draw(self.display)

            #Refresh display and set FPS to 60
            pygame.display.flip()
            clock.tick(60)


Screen(800,600)

#https://www.youtube.com/watch?v=LrcMOeUN1qI
#https://stackoverflow.com/questions/35642629/using-classes-in-pygame
#https://www.piskelapp.com/p/agxzfnBpc2tlbC1hcHByEwsSBlBpc2tlbBiAgKDd4MKkCAw/edit


