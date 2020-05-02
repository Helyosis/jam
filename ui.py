import pygame
class Ui(pygame.sprite.Sprite):
    def __init__(self, width , height, x = 0, y = 0):
        super().__init__()
        self.width=width
        self.height=height

        self.image=pygame.image.load("assets/ui.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height)).convert_alpha()
        self.rect = self.image.get_rect()
        