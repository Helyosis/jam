import pygame
from utils import rotate

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        super().__init__()
        self.game = game

        self.WIDTH, self.HEIGHT = 100, 150
        self.CHAR_WIDTH, self.CHAR_HEIGHT = 50, 50
        self.CONE_WIDTH, self.CONE_HEIGHT = 100, 50

        self.character = pygame.transform.smoothscale(pygame.image.load("assets/scientist.png").convert_alpha(), (self.CHAR_WIDTH, self.CHAR_HEIGHT))
        self.original_cone = self.detection_cone = pygame.transform.smoothscale(pygame.image.load("assets/cone.png").convert_alpha(), (self.CONE_WIDTH, self.CONE_HEIGHT))

        self.cone_angle = 0 #Is in degrees, 90 -> cone is looking up; -90 -> cone is looking down
        self.delta_angle = 1

        self._update_image(self.original_cone, (0, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hitbox = self.character.get_rect()
        self.hitbox.x = x + 50
        self.hitbox.y = y + 50

        self.mask = pygame.mask.from_surface(self.character)

    def _update_image(self, new_cone, coordinates):
        """
        Update the position (and angle) of the detection cone.
        coordinates: coordinates relative to the surface
        """
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.blit(self.character, (50, 50))
        self.image.blit(new_cone, coordinates)
        self.image.set_colorkey((0,0,0))

        #pygame.draw.circle(self.image, (255,255,255), self.detection_cone.get_rect().center, 2)

    def _sweep_cone(self):
        self.cone_angle += self.delta_angle
        if not -75 < self.cone_angle < 75:
            self.delta_angle *= -1
        
            
        new_cone, coordinates = rotate(self.original_cone, (50, 75), (50, 25), self.cone_angle)
        self._update_image(new_cone, coordinates)




    def update(self):
        self._sweep_cone()