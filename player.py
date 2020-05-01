import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.image = pygame.image.load("player.png").convert_alpha()
        self.rect = self.image.get_rect(left=self.x, bottom=self.y)

    
    def move(self, deltax, deltay):
        self.x += deltax
        self.y += deltay

    def update(self):
        pass