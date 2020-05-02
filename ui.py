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
        self.text_queue=text
        self.text_t()
        pygame.draw.rect(self.image, (255,255,255), pygame.Rect(self.x,self.y, width_carre, height_carre))
        self.draw_rate=0
        self.nbchr=0
        self.hp='assets/hp1.png'
        self.hp_image=pygame.transform.scale(pygame.image.load(self.hp), (10, 30)).convert_alpha()
        self.image.blit(self.hp_image,(10,10))
        self.timer(10000)
    def draw_text(self,display,x,y, width, height,text,width_carre,height_carre):
        if self.text != '':
            font = pygame.font.SysFont(pygame.font.get_default_font(),30)
            for i in range(len(self.text)):
                text = font.render(self.text[i], 1, (0,0,0))
                self.image.blit(text,(self.x+(self.width_carre/2 - text.get_width()/2)-240,self.y+(self.height_carre/2 - text.get_height()/2)-80))#240 80
                #self.image.blit(text,(self.x-(self.width_carre/2 - text.get_width()/2),self.y-(self.height_carre/2 - text.get_height()/2)))
                #self.display.blit(text,(0,0))
    def text_t(self):
        self.text_queue=self.text_queue.split(' ')
        self.text = list(self.text_queue)
        line=0
        decallage = 0
        for k in range(len(self.text_queue)):
            if len(self.text_queue[k])+line<23:
                line+=len(self.text_queue[k])
            else:
                self.text.insert(k+decallage,'|')
                decallage += 1
                line=0
        self.text_queue=self.text
        self.text_queue=" ".join(self.text_queue)
        self.text_queue=list(self.text_queue)
    def timer(self,time):
        time=str(time)
        font = pygame.font.SysFont(pygame.font.get_default_font(),30)
        time = font.render(time, 1, (0,0,0))
        self.image.blit(time,(50,10))

    def update(self):
        self.keys = pygame.key.get_pressed()
        if self.draw_rate==0 and self.y<550:
            if len(self.text_queue)>0: 
                self.text = self.text_queue.pop(0)
                if self.text!='|':
                    if self.text==' ' and self.nbchr==0:
                        print('espace en moin')
                        self.text = self.text_queue.pop(0)
                    self.draw_text(self.display,self.x,self.y, self.width, self.height,self.text,self.width_carre,self.height_carre)
                    self.nbchr+=1
                    self.x+=13
                else:
                    self.text = self.text_queue.pop(0)
                    self.y+=20
                    self.x=self.x_0
                    self.nbchr=0
                    self.draw_text(self.display,self.x,self.y, self.width, self.height,self.text,self.width_carre,self.height_carre)
                    self.nbchr+=1
                    self.x+=13
            self.draw_rate=1

        elif self.keys[pygame.K_RETURN] and self.y>=550:
            self.y=self.y_0
            self.x=self.x_0
            pygame.draw.rect(self.image, (255,255,255), pygame.Rect(self.x_0,self.y_0, self.width_carre, self.height_carre))
        else:
            self.draw_rate=0
            