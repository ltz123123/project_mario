import pygame as pg


class character(object):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.left = False
        self.right = False
        self.walk_tick = 0
        self.dy = 0
        self.width = 10
        self.height = 20
        self.vel = 5
        self.jumping = False
        self.img = img

    def jump(self):
        self.dy = -13

    def hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

    def head(self):
        return pg.Rect(self.x, self.y, self.width, self.height * 0.2)

    def feet(self):
        return pg.Rect(self.x, self.y + self.height * 0.8, self.width, self.height * 0.2)

    def draw(self, window):
        if self.walk_tick + 1 > 40:
            self.walk_tick = 0
        if not self.jumping:
            if self.left:
                window.blit(self.img[self.walk_tick // 10], (self.x, self.y))
                self.walk_tick += 1
            elif self.right:
                window.blit(self.img[self.walk_tick // 10], (self.x, self.y))
                self.walk_tick += 1
            else:
                window.blit(self.img[self.walk_tick // 10], (self.x, self.y))
        else:
            window.blit(self.img[4], (self.x, self.y))
            self.walk_tick += 1


class enemy(character):
    def __init__(self, x, y, img):
        character.__init__(self, x, y, img)
        self.width = 15
        self.height = 15
        self.vel = 2
        self.right = True
        self.dy = 0

    def run(self):
        if self.left:
            self.x -= self.vel
        elif self.right:
            self.x += self.vel

    def draw(self, window):
        pg.draw.rect(window,(255,255,255),(self.x,self.y,self.width,self.height),3)

