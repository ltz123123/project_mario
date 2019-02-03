import pygame as pg

class wt_on_earth():#block = (x,y,width,height)
    def __init__(self,block_tuple):
        self.x = block_tuple[0]
        self.y = block_tuple[1]
        self.width = block_tuple[2]
        self.height = block_tuple[3]


    def block(self):
        return pg.Rect(self.x,self.y,self.width,self.height)
    def earth(self):
        return pg.Rect(self.x,self.y - 4,self.width,4)
    def draw(self,mario,screen):
        if self.x - mario.x < 4500:
            pg.draw.rect(screen, (0, 255, 0), (self.x,self.y,self.width,self.height))
