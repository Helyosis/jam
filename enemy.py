import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.WIDTH, self.HEIGHT = 100, 50
        self.CHAR_WIDTH, self.CHAR_HEIGHT = 50, 50
        self.CONE_WIDTH, self.CONE_HEIGHT = 100, 50

        self.character = pygame.transform.scale(pygame.image.load("assets/scientist.png").convert_alpha(), (self.CHAR_WIDTH, self.CHAR_HEIGHT))
        self.detection_cone = pygame.transform.smoothscale(pygame.image.load("assets/cone.png").convert_alpha(), (200, 100))

        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.blit(self.character, (50, 0))
        self.image.blit(self.detection_cone, (0, 0))

        #self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.mask = pygame.mask.from_surface(self.image)