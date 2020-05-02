import pygame
from pygame.locals import *
import sys
from button import Button 
from player import Player
from floor import Floor
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
        background= pygame.image.load("menu.png")
        background.convert()
        self.display.blit(background, (0,0))
        print('requete d\'un super boutton')
        super_boutton=Button(self.display,200,200,400,200,'',mouse_pos,'boutton.png')
        while self.menu_launched:
            for event in pygame.event.get():
                mouse_pos=pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if super_boutton.clic(mouse_pos):
                        self.menu_launched=False
                        self.game_launched=True
                        
                if event.type == pygame.MOUSEMOTION:
                    if super_boutton.clic(mouse_pos):
                        Button(self.display,200,200,400,200,'',mouse_pos,'boutton1.png')
                    else:
                        Button(self.display,200,200,400,200,'',mouse_pos,'boutton.png')

                if event.type == pygame.QUIT:
                    menu_launched = False
                    pygame.quit()
                pygame.display.flip()
#------------------------------------------------------------
    def game_0(self):
        all_sprites = pygame.sprite.Group()
        collide_with_player = pygame.sprite.Group()
        clock = pygame.time.Clock()

        player_character = Player(50, 50, collide_with_player)
        all_sprites.add(player_character)

        floor = Floor(x = 100, y = 300)
        all_sprites.add(floor)
        collide_with_player.add(floor)
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


