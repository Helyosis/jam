import pygame
class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y ):
        super().__init__()
        self.x=x
        self.y=y
        self.WIDTH = 10
        self.HEIGHT = 10
        self.image=pygame.transform.smoothscale(pygame.image.load("assets/coin.png"), (self.WIDTH, self.HEIGHT)).convert_alpha()
        self.rect = self.image.get_rect()
 