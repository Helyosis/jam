[33mcommit bb3c45617c6fa96891afc4802e7794db6708abb7[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m)[m
Merge: 67eeb90 a930ed2
Author: tlefeuvre-22 <tlefeuvre22@gmail.com>
Date:   Sat May 2 22:44:59 2020 +0200

    Merge branch 'master' of https://github.com/Helyosis/jam

[1mdiff --cc bullet.py[m
[1mindex 54987d0,85f4b44..f75bc4d[m
[1m--- a/bullet.py[m
[1m+++ b/bullet.py[m
[36m@@@ -1,22 -1,17 +1,26 @@@[m
  import pygame[m
[32m++<<<<<<< HEAD[m
[32m +from enemy import Enemy[m
[32m++=======[m
[32m+ [m
[32m++>>>>>>> a930ed24ec8c55c940484653264399ae827ce8d6[m
  class Bullet(pygame.sprite.Sprite):[m
[31m -    def __init__(self, x, y, width, height,direction):[m
[32m +    #def __init__(self, x, y, width, height,speed,direction):[m
[32m +    def __init__(self):[m
          super().__init__()[m
[31m -        self.x=x[m
[31m -        self.y=y[m
[31m -        self.width=width[m
[31m -        self.height=height[m
[31m -        self.direction=direction[m
[31m -        self.rect =pygame.Rect(self.x,self.y, self.width, self.height)[m
[32m +        self.width=10[m
[32m +        self.height=10[m
[32m +        self.speed=5[m
[32m +        self.direction=1[m
[32m +        #self.all_bullets = pygame.sprite.Group()[m
          self.image=pygame.image.load("assets/bullet.png")[m
          self.image = pygame.transform.scale(self.image, (30, 30)).convert_alpha()[m
[31m -        self.mouve_forward(10)[m
[31m -    [m
[31m -    def mouve_forward(self, vitesse):[m
[31m -        self.rect.x += (vitesse * self.direction)[m
[32m +        self.rect=self.image.get_rect()[m
[32m +        self.rect.x= Enemy.hitbox.x[m
[32m +        self.rect.y= Enemy.hitbox.y[m
[32m +[m
[32m +        #self.mouv_forward()[m
[32m +    def launch_bullet(self):[m
[32m +        self.all_bullets.add(Bullet())[m
[32m +    def mouv_forward(self):[m
[32m +        self.rect.x += (self.speed * self.direction)[m
[1mdiff --cc enemy.py[m
[1mindex 660c9fc,efa4143..2f82890[m
[1m--- a/enemy.py[m
[1m+++ b/enemy.py[m
[36m@@@ -99,9 -95,10 +99,16 @@@[m [mclass Enemy(pygame.sprite.Sprite)[m
              self._sweep_cone()[m
  [m
          if self.detect_collision():[m
[32m++<<<<<<< HEAD[m
[32m +            self.fire()[m
[32m +        self.all_bullets.draw(self.display) [m
[32m +           [m
[32m++=======[m
[32m+             bullet=Bullet(self.hitbox.x,self.hitbox.y,10,10,5)[m
[32m+             bullet.add(self.game.all_sprites, self.game.characters)[m
[32m+             print('RIFEL')[m
[32m+ [m
[32m++>>>>>>> a930ed24ec8c55c940484653264399ae827ce8d6[m
          if self.rect.right < self.max_x:[m
              pass[m
              #self.move_character(1)[m
