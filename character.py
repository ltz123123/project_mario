import pygame as pg

class character(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

        self.width = 10
        self.height = 20
        self.vel = 4
        self.jumping = False
        self.jumpspeed = 5
        self.jc = 16
        self.jumpCount = 16
    def hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)
    def accelerate():
        ''
    def jump(self,colli,map):
        if self.jumpCount >= -self.jc:
            if self.jumpCount > 0:
                self.y -= self.jumpspeed
                if colli(map):
                    self.y += self.jumpspeed
                    self.jumping = False
                    self.jumpCount = self.jc
            else:
                self.y += self.jumpspeed
                if colli(map):
                    self.y -= self.jumpspeed
                    self.jumping = False
                    self.jumpCount = self.jc
            self.jumpCount -= 1
        else:
            self.jumping = False
            self.jumpCount = self.jc
    def draw(self,screen):
        pg.draw.rect(screen,(255,255,255),self.hitbox())
