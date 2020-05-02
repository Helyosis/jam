import pygame
from utils import collided, rotate
from math import sqrt
from bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, game, ground_sprite):
        """
        Coordinates provided are relative to the characters. Detection cone is added on the fly
        """
        super().__init__()
        self.game = game
        self.min_x, self.max_x = ground_sprite.rect.left, ground_sprite.rect.right

        self.CHAR_WIDTH, self.CHAR_HEIGHT = 50, 50
        self.CONE_WIDTH, self.CONE_HEIGHT = 100, 50
        self.WIDTH, self.HEIGHT = sqrt(self.CONE_WIDTH ** 2 + (self.CONE_HEIGHT / 2) ** 2) + 50, 150

        self.character = pygame.transform.smoothscale(pygame.image.load("assets/scientist.png").convert_alpha(), (self.CHAR_WIDTH, self.CHAR_HEIGHT))
        self.original_cone = self.detection_cone = pygame.transform.smoothscale(pygame.image.load("assets/cone.png").convert_alpha(), (self.CONE_WIDTH, self.CONE_HEIGHT))

        self.cone_angle = 0 #Is in degrees, 90 -> cone is looking up; -90 -> cone is looking down
        self.delta_angle = 1
        self.counter = 0 #Used for slowing cone sweeping when self.game.slow_time == True

        self.hitbox = self.character.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.blit(self.character, (x, y))
        self.image.blit(self.original_cone, (0, 50))
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = x + self.CHAR_WIDTH - self.WIDTH
        self.rect.y = y + self.CHAR_HEIGHT - self.HEIGHT

    def _update_image(self, new_cone, coordinates):
        """
        Update the position (and angle) of the detection cone.
        coordinates: coordinates relative to the surface
        """
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.blit(self.character, (self.rect.x + self.WIDTH - self.CHAR_WIDTH, self.rect.centery - (self.CHAR_HEIGHT/2)))
        self.image.blit(new_cone, coordinates)
        self.image.set_colorkey((0,0,0))

    def move_character(self, dx):
        #TODO: Implement gravity
        #TODO: Add animations when walking
        self.rect.x += dx
        self.hitbox.x += dx

        #pygame.draw.circle(self.image, (255,255,255), self.detection_cone.get_rect().center, 2)

    def _sweep_cone(self):
        self.cone_angle += self.delta_angle
        if not -75 < self.cone_angle < 75:
            self.delta_angle *= -1
        
        new_cone, coordinates = rotate(self.original_cone, (50, 75), (50, 25), self.cone_angle)
        self._update_image(new_cone, coordinates)
        self.detection_cone = new_cone

    def detect_collision(self):
        """
        Detect if cone of Enemy is colliding with Player. If so returns True, else return False
        """
        return pygame.sprite.collide_mask(self, self.game.player_character) and not collided(self, self.game.player_character)

    def fire(self):
        pass

    def update(self):
        if self.game.slow_time:
            if self.counter == 0:
                self._sweep_cone()
            self.counter += 1
            self.counter = self.counter % 5
        else:
            self._sweep_cone()

        if self.detect_collision():
            bullet=Bullet(self.hitbox.x,self.hitbox.y,10,10,5)
            bullet.add(self.game.all_sprites,self.game.characters)
            print('RIFEL')

        if self.rect.right < self.max_x:
            pass
            #self.move_character(1)