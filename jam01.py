import pygame

pygame.init()
launched = True
xScreen=400
yScreen=400

screen= pygame.display.set_mode((xScreen, yScreen), pygame.RESIZABLE)
pygame.display.set_caption("Jeu_trop_bien")

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
