import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height,direction):
        super().__init__()
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.direction=direction
        self.rect =pygame.Rect(self.x,self.y, self.width, self.height)
        self.image=pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (30, 30)).convert_alpha()
        self.mouve_forward(10)
    
    def mouve_forward(self, vitesse):
        self.rect.x += (vitesse * self.direction)
