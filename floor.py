import pygame
WHITE = (255,255,255)

class Floor(pygame.sprite.Sprite):
    def __init__(self, width = 400, height = 20, x = 0, y = 0, color = (255,0,0)):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        #pygame.draw.rect(self.image, color, pygame.Rect(0,0, width, height))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.hitbox = self.rect