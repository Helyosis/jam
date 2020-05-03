import pygame
from utils import collided
import math
import threading, time

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        super().__init__()

        self.WIDTH = 50
        self.HEIGHT = 70

        self.remaining_health = 3
        self.is_dead = False

        self.speed = 5
        self.jump_initial_speed = 15
        self.jump_time = 0
        self.MAX_JUMP_TIME = 20
        self.keys_pressed = []
        self.direction = 0

        self.dx = self.dy = 0
        self.MAX_DX = 5

        #self.image = pygame.image.load("player.png").convert_alpha()
        self.images = {
            "LOOK_RIGHT": pygame.transform.scale(pygame.image.load("assets/player.png").convert_alpha(), (self.WIDTH, self.HEIGHT))
        }
        self.images["LOOK_LEFT"] = pygame.transform.flip(self.images["LOOK_RIGHT"], True, False)

        self.image = self.images["LOOK_RIGHT"]
        self.mask = pygame.mask.from_surface(self.image)
        self.image.set_colorkey((0, 0, 0))


        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.hitbox = self.rect

        self.game = game
        self.colliding_with = self.game.collide_with_player


    def move(self, deltax, deltay):
        self.move_one_axis(deltax, 0)
        self.move_one_axis(0, deltay)

    def force_move(self, dx = 0, dy = 0):
        """
        Force the sprite to move with no regards to collisions. Used by the screen scroller usually.
        """

        self.rect.x += dx
        self.rect.y += dy

    def move_one_axis(self, deltax, deltay):
        if deltax != 0:
            self.rect.x += min(self.MAX_DX, max(-self.MAX_DX, deltax))
            #self.hitbox.x += min(self.MAX_DX, max(-self.MAX_DX, deltax))
        if deltay != 0:
            self.rect.y += deltay
            #self.hitbox.y += deltay

        self._handle_collision(deltax, deltay)

    def _handle_movement(self):
        new_direction = None
        keys = pygame.key.get_pressed()
        new_keys = [k for k, state in enumerate(keys) if k not in self.keys_pressed and state]

        if pygame.K_UP in new_keys:
            self.jump(self.jump_initial_speed)
        
        if pygame.K_DOWN in new_keys:
            pass
        
        if pygame.K_RIGHT in new_keys or (keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
            new_direction = 1

        elif pygame.K_LEFT in new_keys or (keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            new_direction = -1

        if pygame.K_SPACE in new_keys: #TODO: Create config file for keys changes
            if self.game.slow_time <= 0:
                slow_time_thread = threading.Thread(target=self.trigger_slow_time, args=(5,))
                slow_time_thread.start()

        if keys[pygame.K_KP6] or keys[pygame.K_d]:
            self.game.scroll(dx = -3)

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
           new_direction = 0
        
        if new_direction is not None and new_direction != self.direction:
            if new_direction == -1:
                self.image = self.images["LOOK_LEFT"]
            if new_direction == 1:
                self.image = self.images["LOOK_RIGHT"]

        if new_direction is not None:
            self.direction = new_direction

        self.dx += self.speed * self.direction

        self.keys_pressed = [k for k, state in enumerate(keys) if state]


    def _handle_collision(self, dx, dy):
        colliding_sprites = pygame.sprite.spritecollide(self, self.colliding_with, False, collided)
        for sprite in colliding_sprites:
            if dx > 0 : # Moving right; Hit the left side of the sprite
                self.rect.right = sprite.hitbox.left
                self.dx = 0
            if dx < 0: # Moving left; Hit the right side of the sprite
                self.rect.left = sprite.hitbox.right
                self.dx = 0
            if dy > 0: # Moving down; Hit the top side of the sprite
                self.rect.bottom = sprite.hitbox.top
                self.dy = 0
                self.dx = int(self.dx / 2)
                self.jump_time = 0
            if dy < 0: # Moving up; Hit the bottom side of the sprite
                self.rect.top = sprite.hitbox.bottom
                self.dy = 0
        

    def _apply_gravity(self):
        self.dy += 1

    def trigger_slow_time(self, duration):
        """
        Triggers the slowing time power of the Player. It slow every other objets (enemy, lasers, moving platforms...)
        The effect last for durations seconds. Must run in a separate thread to not block other processes
        duration: duration of the time slowing effect
        """
        self.game.slow_time = 5 * 60 #5 * 60 frames = 5 secondess
        print("Le ralentissement commence.")
        time.sleep(duration)
        self.game.slow_time = False
        print("Le temps reprends normalement.")


    def jump(self, force):
        if self.jump_time == 0:
            self.dy -= force
            self.jump_time += 1

    def damage(self, n):
        if n > 0:
            self.remaining_health -= n
            self.game.ui.print(f"OUCH ! -{n} dégats")
            if self.remaining_health <= 0:
                self.game.ui.print("Oh nan :( Te voilà décédé maintenant.")
                self.is_dead = True


    def update(self):
        if not self.is_dead:
            self._handle_movement()
        self._apply_gravity()
        if self.rect.bottom > 380:
            self.rect.bottom = 380

        self.move(self.dx, self.dy)

        if self.game.slow_time >= 0:
            self.game.slow_time -= 1