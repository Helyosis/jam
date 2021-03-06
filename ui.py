import pygame

NEWLINE = '|'

class Ui(pygame.sprite.Sprite):
    def __init__(self,display, width , height,width_carre,height_carre, x, y,text, game):
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
        self.game = game
        self.image=pygame.image.load("assets/ui.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height)).convert_alpha()
        self.rect = self.image.get_rect()
        #self.draw_text(self.display,x,y, width, height,text,width_carre,height_carre)
        self.text_queue=text
        self.text_t()
        pygame.draw.rect(self.image, (255,255,255), pygame.Rect(self.x,self.y, width_carre, height_carre))
        self.draw_rate=0
        self.nbchr=0
        self.hp='assets/hp3.png'
        self.hp_image=pygame.transform.scale(pygame.image.load(self.hp), (150, 50)).convert_alpha()
        self.image.blit(self.hp_image,(10,10))
        self.time_rate =0
        #self.timer(10000)
    def draw_text(self,display,x,y, width, height,text,width_carre,height_carre):
        if self.text != '':
            font = pygame.font.SysFont(pygame.font.get_default_font(),30)
            for i in range(len(self.text)):
                text = font.render(self.text[i], 1, (0,0,0))
                self.image.blit(text,(self.x+(self.width_carre/2 - text.get_width()/2)-240,self.y+(self.height_carre/2 - text.get_height()/2)-80))#240 80
                #self.image.blit(text,(self.x-(self.width_carre/2 - text.get_width()/2),self.y-(self.height_carre/2 - text.get_height()/2)))
                #self.display.blit(text,(0,0))
    def print_hp(self, hp):
        if hp>=0:
            self.hp='assets/hp'+str(hp)+'.png'
            self.hp_image=pygame.transform.scale(pygame.image.load(self.hp), (150, 50)).convert_alpha()
            self.image.blit(self.hp_image,(10,10)) 
            
    def text_t(self):
        self.text_queue=self.text_queue.split(' ')
        self.text = list(self.text_queue)
        line=0
        decallage = 0
        for k in range(len(self.text_queue)):
            if len(self.text_queue[k])+line<23:
                if self.text_queue[k] != '|':
                    line+=len(self.text_queue[k])
                else:
                    line=0
            else:
                self.text.insert(k+decallage, NEWLINE)
                decallage += 1
                line=0
        self.text_queue=self.text
        self.text_queue=" ".join(self.text_queue)
        self.text_queue=list(self.text_queue)


    def timer(self,time):
        if self.time_rate ==0:
            time = 'Time :'+str(time)
            font = pygame.font.SysFont(pygame.font.get_default_font(),30)
            time = font.render(time, 1, (0,0,0))
            pygame.draw.rect(self.image, (255,255,255), pygame.Rect(200,25, 120, 20))
            self.image.blit(time,(200,25))
            self.timer_rate=1
        else:
            self.timer_rate=0

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
                elif len(self.text_queue) > 0:
                    self.text = self.text_queue.pop(0)
                    self.y+=20
                    self.x=self.x_0
                    self.nbchr=0
                    self.draw_text(self.display,self.x,self.y, self.width, self.height,self.text,self.width_carre,self.height_carre)
                    self.nbchr+=1
                    self.x+=13
            self.draw_rate=1

        elif self.keys[pygame.K_RETURN] and self.y>=550:
            self.clear_text()
        else:
            self.draw_rate=0


    def print(self, text_to_print, end = NEWLINE, clear = False):
        """
        Wrapper to print new text and end the text with end arg.
        If clear == True: clear the actual text printed and print the new one.
        """
        self.clear_text()
        self.text_queue = text_to_print + end
        self.text_t()

        print(text_to_print, end = end)
        
    def clear_text(self):
        self.y=self.y_0
        self.x=self.x_0
        pygame.draw.rect(self.image, (255,255,255), pygame.Rect(self.x_0,self.y_0, self.width_carre, self.height_carre))