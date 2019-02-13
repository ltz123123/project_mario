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

    def head(self):
        return pg.Rect(self.x, self.y, self.width, self.height * 0.2)

    def hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

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


class enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15
        self.vel = 1.5
        self.left = True
        self.right = False
        self.dy = 0
        self.spawned = False
        self.lp = 1

    def run(self):
        if self.spawned and self.lp > 0:
            if self.left:
                self.x -= self.vel
            elif self.right:
                self.x += self.vel

    def hit_once(self):
        self.lp -= 1

    def hitbox(self):
        if self.lp == 0:
            return pg.Rect(0, 0, 1, 1)
        return pg.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        if self.spawned and self.lp > 0:
            pg.draw.rect(window, (0, 255, 255), (self.x, self.y, self.width, self.height))


class enemy2(enemy):
    def __init__(self, x, y):
        enemy.__init__(self, x, y)
        self.height = 20
        self.width = 15
        self.lp = 2

    def hit_once(self):
        if self.lp == 2:
            self.height = 15
            self.width = 15
            self.y += 5
            self.vel = 0
        elif self.lp == 1:
            self.vel = 10

        self.lp -= 1


    def hitbox(self):
        if self.lp > 0:
            return pg.Rect(self.x, self.y, self.width, self.height)
        else:
            return pg.Rect(0, 0, 1, 1)


m1 = enemy(435, 265)
m2 = enemy(720, 265)
m3 = enemy(875, 265)
m4 = enemy(895, 265)
m5 = enemy(1360, 135)
m6 = enemy(1385, 135)
m7 = enemy(1615, 265)
m8 = enemy(1640, 265)
m9 = enemy(2060, 265)
m10 = enemy(2085, 265)
m11 = enemy(2110, 265)
m12 = enemy(2130, 265)
m13 = enemy(2815, 265)
m14 = enemy(2840, 265)
t1 = enemy2(1790,260)

all_enemy = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, t1]
