import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, colliding_with):
        super().__init__()

        self.WIDTH = 50
        self.HEIGHT = 70

        self.speed = 5
        self.jump_initial_speed = 15
        self.jump_time = 0
        self.MAX_JUMP_TIME = 20
        self.keys_pressed = []
        self.direction = 0


        self.dx = self.dy = 0
        self.MAX_DX = 5

        #self.image = pygame.image.load("player.png").convert_alpha()
        
        self.image = pygame.image.load("player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.image.set_colorkey((0, 0, 0))


        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        self.colliding_with = colliding_with


    def move(self, deltax, deltay):
        self.move_one_axis(deltax, 0)
        self.move_one_axis(0, deltay)

    def move_one_axis(self, deltax, deltay):
        if deltax != 0:
            self.rect.x += min(self.MAX_DX, max(-self.MAX_DX, deltax))
            self._handle_collision(deltax, deltay)

        if deltay != 0:
            self.rect.y += deltay
            self._handle_collision(deltax, deltay)


    def _handle_movement(self):
        keys = pygame.key.get_pressed()
        new_keys = [k for k, state in enumerate(keys) if k not in self.keys_pressed and state]

        if pygame.K_UP in new_keys:
            self.jump(self.jump_initial_speed)
        
        
        if pygame.K_DOWN in new_keys:
            pass
        
        if pygame.K_RIGHT in new_keys or (keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
            self.direction = 1
        elif pygame.K_LEFT in new_keys or (keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.direction = -1
       
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
           self.direction = 0

        self.dx += self.speed * self.direction

        self.keys_pressed = [k for k, state in enumerate(keys) if state]

        

    def _handle_collision(self, dx, dy):
        colliding_sprites = pygame.sprite.spritecollide(self, self.colliding_with, False, pygame.sprite.collide_mask)
        for sprite in colliding_sprites:
            if dx > 0 : # Moving right; Hit the left side of the sprite
                self.rect.right = sprite.rect.left
                self.dx = 0
            if dx < 0: # Moving left; Hit the right side of the sprite
                self.rect.left = sprite.rect.right
                self.dx = 0
            if dy > 0: # Moving down; Hit the top side of the sprite
                self.rect.bottom = sprite.rect.top
                self.dy = 0
                self.dx = int(self.dx / 2)
                self.jump_time = 0
            if dy < 0: # Moving up; Hit the bottom side of the sprite
                self.rect.top = sprite.rect.bottom
                self.dy = 0
        
    def _apply_gravity(self):
        self.dy += 1

    def jump(self, force):
        if self.jump_time == 0:
            self.dy -= force
            self.jump_time += 1
    def update(self):
        self._handle_movement()
        self._apply_gravity()

        self.move(self.dx, self.dy)
