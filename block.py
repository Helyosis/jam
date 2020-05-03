import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0, width = 20, height = 20, game = None, texture = (255,0,0), path = list()):
        """
        Create a block
        """
        super().__init__()
        self.game = game
        #assert self.game is not None
        
        if type(texture) == type(tuple()):
            self.image = pygame.Surface((width, height))
            self.image.fill(texture)
        else:
            #texture is a filepath to asset
            self.image = pygame.image.smoothscale(pygame.image.load(texture).convert_alpha(), (width, height))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.hitbox = self.rect
        
        self.counter = 0

        self.path = path

    def force_move(self, dx = 0, dy = 0):
        """
        Force the sprite to move. Used by the screen scroller usually.
        """

        self.rect.x += dx
        self.rect.y += dy

    def update(self):
        if (self.game.slow_time > 0 and self.counter == 0) or self.game.slow_time <= 0:
            if len(self.path) > 0:
                new_pos = self.path.pop(0)
                self.path.append(new_pos)
                self.force_move(*new_pos)
        
        self.counter += 1
        self.counter = self.counter % 5