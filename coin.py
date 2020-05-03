import pygame
class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y, game):
        super().__init__()

        self.game=game
        self.WIDTH = 50
        self.HEIGHT = 50
        self.image=pygame.transform.smoothscale(pygame.image.load("assets/coin.png"), (self.WIDTH, self.HEIGHT)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hitbox = self.rect

    def collision(self):
        colliding_sprites = pygame.sprite.collide_mask(self, self.game.player_character)
        if colliding_sprites:
            self.game.coin+=1
            self.kill()
            del self
    
    def force_move(self, dx = 0, dy = 0):
        """
        Force the sprite to move. Used by the screen scroller usually.
        """

        self.rect.x += dx
        self.rect.y += dy
