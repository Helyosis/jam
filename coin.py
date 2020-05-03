import pygame
<<<<<<< HEAD
class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y, game):
        super().__init__()
        self.x=x
        self.y=y
        self.game=game
        self.WIDTH = 10
        self.HEIGHT = 10
        self.image=pygame.transform.smoothscale(pygame.image.load("assets/coin.png"), (self.WIDTH, self.HEIGHT)).convert_alpha()
        self.rect = self.image.get_rect()
        self.hitbox = self.rect
        self.add(self.game.all_sprites, self.game.all_game_objects, self.game.projectiles)
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
=======

class Coin(pygame.sprite.Srite):
    def __init__(self, x, y):
        super().__init__()
        
>>>>>>> 7cfd8b52f8c4330f524905c4b1ff2b4ee58b7246
