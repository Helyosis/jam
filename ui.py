import pygame
class Ui(pygame.sprite.Sprite):
    def __init__(self,display, width , height,width_carre,height_carre, x, y,text):
        super().__init__()
        self.display=display
        self.width=width
        self.height=height
        self.width_carre=width_carre
        self.height_carre=height_carre
        self.x=x
        self.y=y
        self.x_0=x
        self.y_0=y
        self.text=text
        self.image=pygame.image.load("assets/ui.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height)).convert_alpha()
        self.rect = self.image.get_rect()
        #self.draw_text(self.display,x,y, width, height,text,width_carre,height_carre)
        self.text_queue=list(self.text)
        pygame.draw.rect(self.image, (255,255,255), pygame.Rect(self.x,self.y, width_carre, height_carre))

    def draw_text(self,display,x,y, width, height,text,width_carre,height_carre):
        if self.text != '':
            font = pygame.font.SysFont(pygame.font.get_default_font(),30)
            for i in range(len(self.text)):
                text = font.render(self.text[i], 1, (0,0,0))
                self.image.blit(text,(self.x+(self.width_carre/2 - text.get_width()/2)-240,self.y+(self.height_carre/2 - text.get_height()/2)-80))#240 80
                #self.image.blit(text,(self.x-(self.width_carre/2 - text.get_width()/2),self.y-(self.height_carre/2 - text.get_height()/2)))
                #self.display.blit(text,(0,0))
                self.x+=15
                
    def update(self):
        if len(self.text_queue)>0: 
            self.text = self.text_queue.pop(0)
            if self.text!='|':
                self.draw_text(self.display,self.x,self.y, self.width, self.height,self.text,self.width_carre,self.height_carre)
            else:
                print('retourrrrrrrrrr')
                self.y+=20
                self.x=self.x_0
                if self.y>500:
                    self.y=self.y_0
                    pygame.draw.rect(self.image, (255,255,255), pygame.Rect(self.x,self.y, self.width_carre, self.height_carre))
