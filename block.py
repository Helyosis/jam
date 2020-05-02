import pygame
WHITE = (255,255,255)

class Block(pygame.sprite.Sprite):
    def __init__(self, width = 20, height = 20, x = 0, y = 0, color = (255,0,0)):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        #pygame.draw.rect(self.image, color, pygame.Rect(0,0, width, height))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.hitbox = self.rect

    def force_move(self, dx = 0, dy = 0):
        """
        Force the sprite to move. Used by the screen scroller usually.
        """

        self.rect.x += dx
        self.rect.y += dy