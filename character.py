import pygame as pg


class character(object):
    def __init__(self, x, y, img_s, img_l, img_r):
        self.x = x
        self.y = y
        self.left = False
        self.right = True
        self.standing = True
        self.walk_tick = 0
        self.dy = 0
        self.width = 10
        self.height = 20
        self.vel = 5
        self.jumping = False
        self.img_s = img_s
        self.img_l = img_l
        self.img_r = img_r

    def jump(self):
        self.dy = -12

    def hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

    def head(self):
        return pg.Rect(self.x, self.y, self.width, self.height * 0.2)

    def draw(self, window):
        if self.walk_tick + 1 > 25:
            self.walk_tick = 0
        if not self.jumping:
            if self.standing:
                window.blit(self.img_s[0], (self.x, self.y))
            elif self.left:
                window.blit(self.img_l[self.walk_tick // 10], (self.x, self.y))
                self.walk_tick += 1
            elif self.right:
                window.blit(self.img_r[self.walk_tick // 10], (self.x, self.y))
                self.walk_tick += 1
        elif self.jumping:
            if self.left:
                window.blit(self.img_s[1], (self.x, self.y))
            elif self.right:
                window.blit(self.img_s[2], (self.x, self.y))

class enemy(character):
    def __init__(self, x, y, img_s, img_l, img_r):
        character.__init__(self, x, y, img_s, img_l, img_r)
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
        pg.draw.rect(window,(0,255,255),(self.x,self.y,self.width,self.height))

    def head(self):
        return pg.Rect(self.x - 3, self.y, self.width + 6, self.height * 0.2)

