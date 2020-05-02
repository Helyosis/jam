import pygame
from utils import degrees_to_radian
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, startX, startY, firingAngle, game):
        """
        Firing angle is in radian.
        """
        super().__init__()

        self.WIDTH = 10
        self.HEIGHT = 10
        self.SPEED = 5

        self.game = game

        self.firing_angle = firingAngle
        self.dx = math.cos(firingAngle) * self.SPEED
        self.dy = math.sin(firingAngle) * self.SPEED

        self.image=pygame.transform.smoothscale(pygame.image.load("assets/bullet.png"), (self.WIDTH, self.HEIGHT)).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = startX
        self.rect.y = startY


    def update(self):
        if self.game.slow_time and self.SPEED == 5:
            self.SPEED = 1
            self.dx = math.cos(self.firing_angle) * self.SPEED
            self.dy = math.sin(self.firing_angle) * self.SPEED
        elif not self.game.slow_time and self.SPEED == 1:
            self.SPEED = 5
            self.dx = math.cos(self.firing_angle) * self.SPEED
            self.dy = math.sin(self.firing_angle) * self.SPEED

        self.rect.x += self.dx
        self.rect.y += self.dy

    def force_move(self, dx = 0, dy = 0):
        """
        Force the sprite to move. Used by the screen scroller usually.
        """

        self.rect.x += dx
        self.rect.y += dy
