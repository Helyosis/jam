import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, game, damage = 1):
        super().__init__()

        self.WIDTH = 20
        self.HEIGHT = 10
        self.speed = 1
        self.direction = 1

        self.damage = damage

        self.image = pygame.image.load("assets/laser.png")
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT)).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.hitbox = self.rect
        self.time = 0
        self.game = game

    def update(self):
        self.time+=1
        if self.time<=10:
            self.direction=1
        else:
            self.direction=-1
        if self.time==20:
            self.time=0

        self.rect.x += self.speed * self.direction

        colliding_sprites = pygame.sprite.collide_mask(self, self.game.player_character)
        if colliding_sprites:
            if self.direction > 0 : # Moving right; Hit the left side of the sprite
                self.game.player_character.rect.left = self.rect.right 
            if self.direction < 0: # Moving left; Hit the right side of the sprite
                self.game.player_character.rect.right = self.rect.left
