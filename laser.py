import pygame

direction_to_degrees = {
    "UP": 0,
    "DOWN": 180,
    "LEFT": -90,
    "RIGHT": 90
}

class LaserShooter(pygame.sprite.Sprite):
    def __init__(self, x, y, game, direction, max_length = 10, damage = 1, cooldown = 2 * 60, resource = "assets/lasershooter.png"):
        super().__init__()
        self.WIDTH = 20
        self.HEIGHT = 20
        self.game = game

        self.direction = direction
        self.max_length = max_length

        self.image = pygame.image.load(resource)
        self.image = pygame.transform.smoothscale(self.image, (self.WIDTH, self.HEIGHT)).convert_alpha()
        self.image = pygame.transform.rotate(self.image, direction_to_degrees[direction])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.hitbox = self.rect
        
        self.cooldown = cooldown
        self.timer = self.cooldown

    def force_move(self, dx = 0, dy = 0):
        """
        Force the sprite to move. Used by the screen scroller usually.
        """

        self.rect.x += dx
        self.rect.y += dy

    def shoot_laser(self):
        self.new_laser = Laser(self.rect.x, self.rect.y, self.direction, self, self.game, self.max_length)

    def try_kill(self):
        pass #Not used here


    def update(self):
        self.timer -= 1
        if self.timer == 0:
            self.shoot_laser()

        if self.timer == -self.cooldown:
            self.new_laser.try_kill()
            self.timer = self.cooldown
    


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, parent, game, remaining_laser, damage = 1):
        super().__init__()

        self.WIDTH = 20
        self.HEIGHT = 10
        self.speed = 10
        self.cooldown = 20

        self.is_dead = False
        
        self.game = game
        self.parent = parent

        convert = {
            "UP": (0, -1),
            "DOWN": (0, 1),
            "LEFT": (-1, 0),
            "RIGHT": (1, 0)
        }

        self.direction = direction
        self.dx, self.dy = convert.get(direction, (0, 0))

        self.damage = damage
        self.counter = 0

        self.image = pygame.image.load("assets/laser.png")
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT)).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.hitbox = self.rect

        self.add(self.game.all_sprites, self.game.all_game_objects, self.game.projectiles)

        self.game = game

    def force_move(self, dx = 0, dy = 0):
        """
        Force the sprite to move. Used by the screen scroller usually.
        """

        self.rect.x += dx
        self.rect.y += dy

    def spawn_laser(self):
        self.new_laser = Laser(self.rect.x + (self.dx * self.speed), self.rect.y + (self.dy * self.speed), self.direction, self, self.game, self.damage)
        
    def try_kill(self):
        if not self.is_dead:
            self.is_dead = True
            self.kill()
            try:
                self.parent.try_kill()
            except AttributeError:
                pass
            try:
                self.new_laser.try_kill()
            except AttributeError:
                pass
            del self
    
    def update(self):
        if ((self.game.slow_time > 0 and self.counter == 0) or self.game.slow_time <= 0) and self.cooldown == 0:
            self.spawn_laser()

        self.cooldown -= 1
        self.counter += 1
        self.counter = self.counter % 5

        colliding_sprites = pygame.sprite.collide_mask(self, self.game.player_character)
        if colliding_sprites:
            self.game.player_character.damage(self.damage)
            self.kill()
            del self
