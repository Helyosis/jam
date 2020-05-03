import pygame
from utils import collided, rotate
from math import sqrt
from bullet import Bullet
from math import sqrt, ceil, atan2, pi, degrees

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
        self.TUBE_WIDTH, self.TUBE_HEIGHT = self.CONE_WIDTH, 10
        self.WIDTH, self.HEIGHT = ceil(sqrt(self.CONE_WIDTH ** 2 + (self.CONE_HEIGHT / 2) ** 2) + 50), 2*self.CONE_WIDTH

        self.character = pygame.transform.smoothscale(pygame.image.load("assets/scientist.png").convert_alpha(), (self.CHAR_WIDTH, self.CHAR_HEIGHT))
        self.original_cone = self.cone = self.detection_cone = pygame.transform.smoothscale(pygame.image.load("assets/cone.png").convert_alpha(), (self.CONE_WIDTH, self.CONE_HEIGHT))
        self.tube = pygame.transform.smoothscale(pygame.image.load("assets/tube.png").convert_alpha(), (self.TUBE_WIDTH, self.TUBE_HEIGHT))

        self.cone_angle = 0 #Is in degrees, 90 -> cone is looking up; -90 -> cone is looking down
        self.delta_angle = 1
        self.counter = 0 #Used for slowing cone sweeping when self.game.slow_time == True

        self.is_shooting = False

        self.hitbox = self.character.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.blit(self.character, (self.WIDTH - self.CHAR_WIDTH, (self.HEIGHT // 2) - (self.CHAR_HEIGHT // 2)))
        self.image.blit(self.original_cone, (self.WIDTH - self.CHAR_WIDTH - self.CONE_WIDTH, self.HEIGHT// 2))
        #self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.right = x + self.CHAR_WIDTH
        self.rect.centery = y + self.CHAR_HEIGHT //2 
        #Very broken but it works

    def _update_image(self, new_cone, coordinates):
        """
        Update the position (and angle) of the detection cone.
        coordinates: coordinates relative to the surface
        """
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT), flags=pygame.SRCALPHA)
        self.image.blit(self.character, (self.WIDTH - self.CHAR_WIDTH, (self.HEIGHT // 2) - (self.CHAR_HEIGHT // 2)))
        self.image.blit(new_cone, coordinates)
        self.mask = pygame.mask.from_surface(self.image, 50) #Create a mask with adequate collision (threshold is low enough so that detection_cone is detected)


    def force_move(self, dx = 0, dy = 0):
        """
        Force the sprite to move. Used by the screen scroller usually.
        """

        self.rect.x += dx
        self.hitbox.x += dx

        self.rect.y += dy
        self.hitbox.y += dy

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
        
        self._rotate_cone(self.cone_angle)       
        

    def _aim_with_cone(self, x, y):
        theta = pi - atan2(y - self.hitbox.centery, x - self.hitbox.x)
        theta = degrees(theta)
        self._rotate_cone(theta)

    def _rotate_cone(self, theta):
        """
        Rotate cone at theta degrees around the pivot symbolised by the end of the cone (near the Enemy character)
        """
        new_cone, coordinates = rotate(self.cone, (self.WIDTH - self.CHAR_WIDTH, self.HEIGHT // 2), (self.CONE_WIDTH, self.CONE_HEIGHT//2), theta)
        self._update_image(new_cone, coordinates)
        self.detection_cone = new_cone  


    def detect_collision(self):
        """
        Detect if cone of Enemy is colliding with Player. If so returns True, else return False
        """
        return pygame.sprite.collide_mask(self, self.game.player_character) and not collided(self, self.game.player_character)

    def shoot(self, x, y):
        theta = pi - atan2(y - self.hitbox.centery, x - self.hitbox.x)
        print(theta)
        bullet = Bullet(self.hitbox.x, self.hitbox.centery, theta, self.game)
        bullet.add(self.game.all_sprites, self.game.all_game_objects, self.game.characters)

    def update(self):
        if (self.game.slow_time and self.counter == 0) or not self.game.slow_time:
            if self.is_shooting:
                if self.is_aiming:
                    self._aim_with_cone(*self.game.player_character.rect.center)

                self.time -= 1
                if self.time == 60: #1 second left
                    self.aimed_at_x, self.aimed_at_y = self.game.player_character.rect.center
                    self.is_aiming = False

                if self.time == 0:
                    self.shoot(self.aimed_at_x, self.aimed_at_y)
                    self.cone = self.original_cone
                    
                if self.time == -60: #1 second after shooting
                    self.is_shooting = False
                    del self.time

            else:
                self._sweep_cone()

            if self.detect_collision() and not self.is_shooting:
                self.is_shooting = self.is_aiming = True
                self.time = 60 * 5 #5 seconds
                reload_sound = pygame.mixer.Sound('assets/reload.wav')
                reload_sound.play()
                self.cone = self.tube

            if self.rect.right < self.max_x:
                pass
                #self.move_character(1)

        self.counter += 1
        self.counter = self.counter % 5