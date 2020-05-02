import pygame
class Button(pygame.sprite.Sprite):
    def __init__(self, display,x,y, width, height,text,mouse_pos,nom_img):
        super().__init__()
        self.width=width
        self.height=height
        self.x=x
        self.y=y
        self.text=text
        self.display=display
        self.nom_img=nom_img

        self.draw_button(display,x,y, width, height,text,nom_img)
        self.mouse_pos=mouse_pos
    def draw_button(self,display,x,y, width, height,text,nom_img):
         self.button = pygame.Surface([width, height])
         boutton= pygame.image.load(nom_img)
         boutton.convert()
         self.display.blit(boutton, (x,y))
         if self.text != '':
            font = pygame.font.SysFont('comicsans',60)
            text = font.render(self.text, 1, (0,0,0))
            self.display.blit(text,(self.x+(self.width/2 - text.get_width()/2),self.y+(self.height/2 - text.get_height()/2)))
    def clic(self, mouse_pos) :
        if mouse_pos[0]>self.x and mouse_pos[0]<self.x+self.width:#and cliked
            if mouse_pos[1]> self.y and mouse_pos[1]<self.y+self.width:
                return True
        return False 

        
        