import pygame

class LaserShooter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.WIDTH = 20
        self.HEIGHT = 20

        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill()