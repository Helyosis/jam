import pygame

def collided(sprite, other):
    return sprite.hitbox.colliderect(other.hitbox)