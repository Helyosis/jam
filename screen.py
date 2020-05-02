import pygame
from pygame.locals import *
import sys
from button import Button
from game import Game

class Screen(object):

    def __init__(self, width, height):
        #------------------
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Jeu_trop_bien")
        self.width=width
        self.height=height
        self.display=pygame.display.set_mode((self.width,self.height))
        self.game = Game(self.width, self.height, self.display)
        #------------------
        self.menu_launched=True
        self.menu()
        self.game.run()
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
        menu_song.play().set_volume(0.3)#nb rep, tmpmax,fondue 0->100s .set_volume(0.5)
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
Screen(800,600)

#https://www.youtube.com/watch?v=LrcMOeUN1qI
#https://stackoverflow.com/questions/35642629/using-classes-in-pygame
#https://www.piskelapp.com/p/agxzfnBpc2tlbC1hcHByEwsSBlBpc2tlbBiAgKDd4MKkCAw/edit


