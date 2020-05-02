import pygame
class Bullet(pygame.sprite.Sprite):
    #def __init__(self, x, y, width, height,speed,direction):
    def __init__(self):
        super().__init__()
        self.width=10
        self.height=10
        self.speed=5
        self.direction=1
        #self.all_bullets = pygame.sprite.Group()
        self.image=pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (30, 30)).convert_alpha()
        self.rect=self.image.get_rect()
        #self.rect.x= Enemy.hitbox.x
        #self.rect.y= Enemy.hitbox.y

        #self.mouv_forward()
    def launch_bullet(self):
        self.all_bullets.add(Bullet())
    #def mouv_forward(self):
    #self.rect.x += (self.speed * self.direction)
