import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        super().__init__()

        self.WIDTH = 20
        self.HEIGHT = 20

        self.image=pygame.image.load("assets/lasert.png")
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT)).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = x
        self.hitbox=self.rect
        self.time=0
        self.game=game
    def update(self):
        self.time+=1
        if self.time<=10:
            self.direction=2
        else:
            self.direction=-2
        if self.time==20:
            self.time=0
        self.rect.x += (self.speed * self.direction)

        colliding_sprites = pygame.sprite.collide_rect(self,self.game.player_character)
        if colliding_sprites:
            if self.direction > 0 : # Moving right; Hit the left side of the sprite
                self.game.player_character.rect.right +=1 
            if self.direction < 0: # Moving left; Hit the right side of the sprite
                self.game.player_character.rect.left -= 1
