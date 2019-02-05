import pygame as pg


class wt_on_earth:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def block(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

    def earth(self):
        return pg.Rect(self.x - 4, self.y - 4, self.width + 8, 4)

    def draw(self, mario, screen):
        if abs(self.x - mario.x) < 1300:
            pg.draw.rect(screen, (47, 79, 79), (self.x, self.y, self.width, self.height))


class Qmark(wt_on_earth):
    def __init__(self, x, y, width, height):
        wt_on_earth.__init__(self, x, y, width, height)
        self.broken = False

    def ceiling(self):
        return pg.Rect(self.x, self.y + self.height, self.width, 4)

    def ceiling_hitbox(self):
        return pg.Rect(self.x + 3, self.y + self.height, self.width - 6, 4)

    def draw(self, mario, screen):
        if abs(self.x - mario.x) < 1300:
            if self.broken:
                pg.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))
            else:
                pg.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.width, self.height))


class brick(wt_on_earth):
    def __init__(self, x, y, width, height):
        wt_on_earth.__init__(self, x, y, width, height)
        self.broken = False

    def block(self):
        if not self.broken:
            return pg.Rect(self.x, self.y, self.width, self.height)
        return pg.Rect(0, 0, 1, 1)

    def earth(self):
        if not self.broken:
            return pg.Rect(self.x - 4, self.y - 4, self.width + 8, 4)
        return pg.Rect(0, 0, 1, 1)

    def ceiling(self):
        if not self.broken:
            return pg.Rect(self.x, self.y + self.height, self.width, 4)
        return pg.Rect(0, 0, 1, 1)

    def ceiling_hitbox(self):
        if not self.broken:
            return pg.Rect(self.x + 3, self.y + self.height, self.width - 6, 4)
        return pg.Rect(0, 0, 1, 1)

    def draw(self, mario, screen):
        if abs(self.x - mario.x) < 1300 and not self.broken:
            pg.draw.rect(screen, (169, 0, 0), (self.x, self.y, self.width, self.height))


# groung
g1 = wt_on_earth(0, 280, 1100, 20)
g2 = wt_on_earth(1135, 280, 240, 20)
g3 = wt_on_earth(1425, 280, 1025, 20)
g4 = wt_on_earth(2480, 280, 820, 20)
# pipe
p1 = wt_on_earth(450, 250, 30, 30)
p2 = wt_on_earth(610, 230, 30, 50)
p3 = wt_on_earth(735, 215, 30, 65)
p4 = wt_on_earth(910, 215, 30, 65)
p5 = wt_on_earth(2610, 250, 30, 30)
p6 = wt_on_earth(2865, 250, 30, 30)
# stair
s11 = wt_on_earth(2145, 265, 15, 15)
s12 = wt_on_earth(2160, 250, 15, 30)
s13 = wt_on_earth(2175, 235, 15, 45)
s14 = wt_on_earth(2190, 220, 15, 60)

s21 = wt_on_earth(2240, 220, 15, 60)
s22 = wt_on_earth(2255, 235, 15, 45)
s23 = wt_on_earth(2270, 250, 15, 30)
s24 = wt_on_earth(2285, 265, 15, 15)

s31 = wt_on_earth(2375, 265, 15, 15)
s32 = wt_on_earth(2390, 250, 15, 30)
s33 = wt_on_earth(2405, 235, 15, 45)
s34 = wt_on_earth(2420, 220, 15, 60)
s35 = wt_on_earth(2435, 220, 15, 60)

s41 = wt_on_earth(2480, 220, 15, 60)
s42 = wt_on_earth(2495, 235, 15, 45)
s43 = wt_on_earth(2510, 250, 15, 30)
s44 = wt_on_earth(2525, 265, 15, 15)

s51 = wt_on_earth(2895, 265, 15, 15)
s52 = wt_on_earth(2910, 250, 15, 30)
s53 = wt_on_earth(2925, 235, 15, 45)
s54 = wt_on_earth(2940, 220, 15, 60)
s55 = wt_on_earth(2955, 205, 15, 75)
s56 = wt_on_earth(2970, 190, 15, 90)
s57 = wt_on_earth(2985, 175, 15, 105)
s58 = wt_on_earth(3000, 160, 15, 120)
s59 = wt_on_earth(3015, 160, 15, 120)
# Question mark block
q1 = Qmark(255, 215, 15, 15)
q2 = Qmark(335, 215, 15, 15)
q3 = Qmark(350, 150, 15, 15)
q4 = Qmark(365, 215, 15, 15)
q5 = Qmark(1250, 215, 15, 15)
q6 = Qmark(1500, 150, 15, 15)
q7 = Qmark(1695, 215, 15, 15)
q8 = Qmark(1745, 215, 15, 15)
q9 = Qmark(1790, 215, 15, 15)
q10 = Qmark(1745, 150, 15, 15)
q11 = Qmark(2065, 150, 15, 15)
q12 = Qmark(2080, 150, 15, 15)
q13 = Qmark(2720, 215, 15, 15)
# brick
b1 = brick(320, 215, 15, 15)
b2 = brick(350, 215, 15, 15)
b3 = brick(380, 215, 15, 15)
b4 = brick(1235, 215, 15, 15)
b5 = brick(1265, 215, 15, 15)
b6 = brick(1280, 150, 15, 15)
b7 = brick(1295, 150, 15, 15)
b8 = brick(1310, 150, 15, 15)
b9 = brick(1325, 150, 15, 15)
b10 = brick(1340, 150, 15, 15)
b11 = brick(1355, 150, 15, 15)
b12 = brick(1370, 150, 15, 15)
b13 = brick(1455, 150, 15, 15)
b14 = brick(1470, 150, 15, 15)
b15 = brick(1485, 150, 15, 15)
b16 = brick(1500, 215, 15, 15)
b17 = brick(1600, 215, 15, 15)
b18 = brick(1890, 215, 15, 15)
b19 = brick(1935, 150, 15, 15)
b20 = brick(1950, 150, 15, 15)
b21 = brick(1965, 150, 15, 15)
b22 = brick(2050, 150, 15, 15)
b23 = brick(2065, 215, 15, 15)
b24 = brick(2080, 215, 15, 15)
b25 = brick(2095, 150, 15, 15)
b26 = brick(2690, 215, 15, 15)
b27 = brick(2705, 215, 15, 15)
b28 = brick(2735, 215, 15, 15)

map = [g1, g2, g3, g4,
       p1, p2, p3, p4, p5, p6,
       s11, s12, s13, s14,
       s21, s22, s23, s24,
       s31, s32, s33, s34, s35,
       s41, s42, s43, s44,
       s51, s52, s53, s54, s55, s56, s57, s58, s59]

map_breakable = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13,
                 b1, b2, b3, b4, b5, b6, b7, b8, b9, b10,
                 b11, b12, b13, b14, b15, b16, b17, b18, b19, b20,
                 b21, b22, b23, b24, b25, b26, b27, b28]
