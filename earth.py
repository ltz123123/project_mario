import pygame as pg


class Wt_on_earth:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def block(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

    def earth(self):
        return pg.Rect(self.x, self.y - 5, self.width, 10)

    def draw(self, ma, window):
        if abs(self.x - ma.x) < 1300:
            pg.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height), 1)


class Stair(Wt_on_earth):
    def __init__(self, x, y, width, height):
        Wt_on_earth.__init__(self, x, y, width, height)

    def draw(self, ma, window):
        if abs(self.x - ma.x) < 1300:
            for i in range(self.height // 15):
                pg.draw.rect(window, (255, 255, 255), (self.x, self.y + 15 * i, 15, 15), 1)

class Pipe(Wt_on_earth):
    def __init__(self, x, y, width, height):
        Wt_on_earth.__init__(self, x, y, width, height)

    def draw(self, ma, window):
        if abs(self.x - ma.x) < 1300:
            pg.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, 15), 1)
            pg.draw.rect(window, (255, 255, 255), (self.x + 3, self.y + 15, self.width - 6, self.height - 15), 1)


class Qmark(Wt_on_earth):
    def __init__(self, x, y):
        Wt_on_earth.__init__(self, x, y, 15, 15)
        self.broken = False
        self.img = pg.image.load('structure/qmark.png')

    def broke(self, a):
        a.dy = 2
        self.broken = True

    def ceiling(self):
        return pg.Rect(self.x, self.y + self.height, self.width, 4)

    def ceiling_hitbox(self):
        return pg.Rect(self.x + 4, self.y + self.height, self.width - 7, 4)

    def draw(self, ma, window):
        if abs(self.x - ma.x) < 1300:
            if self.broken:
                pg.draw.rect(window, (0, 255, 255), (self.x, self.y, self.width, self.height), 1)
            else:
                window.blit(self.img, (self.x, self.y))


class hidden(Qmark):
    def __init__(self, x, y):
        Qmark.__init__(self, x, y)
        self.broken = False

    def block(self):
        if self.broken:
            return pg.Rect(self.x, self.y, self.width, self.height)
        return pg.Rect(4, 0, 1, 1)

    def earth(self):
        if self.broken:
            return pg.Rect(self.x, self.y - 4, self.width, 10)
        return pg.Rect(2, 2, 1, 1)

    def draw(self, ma, window):
        if abs(self.x - ma.x) < 1300:
            if self.broken:
                pg.draw.rect(window, (0, 255, 255), (self.x, self.y, self.width, self.height), 1)


class Brick(Wt_on_earth):
    def __init__(self, x, y):
        Wt_on_earth.__init__(self, x, y, 15, 15)
        self.broken = False

    def broke(self, a):
        self.broken = True
        a.dy = 2

    def block(self):
        if not self.broken:
            return pg.Rect(self.x, self.y, self.width, self.height)
        return pg.Rect(1, 1, 1, 1)

    def earth(self):
        if not self.broken:
            return pg.Rect(self.x - 2, self.y - 4, self.width + 4, 10)
        return pg.Rect(1, 1, 1, 1)

    def ceiling(self):
        if not self.broken:
            return pg.Rect(self.x, self.y + self.height, self.width, 4)
        return pg.Rect(1, 1, 1, 1)

    def ceiling_hitbox(self):
        if not self.broken:
            return pg.Rect(self.x + 3, self.y + self.height, self.width - 6, 4)
        return pg.Rect(1, 1, 1, 1)

    def draw(self, ma, window):
        if not self.broken:
            pg.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height), 1)


class end_point(Wt_on_earth):
    def __init__(self, x, y):
        Wt_on_earth.__init__(self, x, y, 15, 15)
        self.img = pg.image.load('structure/castle.png')

    def pole(self):
        return pg.Rect(self.x + 5, self.y - 200, 5, 200)

    def castle(self):
        return pg.Rect(self.x + 120, self.y - 30, 25, 30)

    def draw(self, mario, window):
        if abs(self.x - mario.x) < 1300:
            pg.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))
            pg.draw.rect(window, (255, 255, 255), (self.x + 7, self.y - 200, 3, 200))
            pg.draw.circle(window, (255, 255, 255), (self.x + 8, self.y - 203), 5, 2)
            pg.draw.polygon(window, (255, 255, 255), [(self.x + 8, self.y - 200), (self.x + 8, self.y - 170), (self.x + 40, self.y - 185)], 3)
            window.blit(self.img, (self.x + 60, self.y - 185))


# ground
g1 = Wt_on_earth(0, 280, 1100, 20)
g2 = Wt_on_earth(1135, 280, 240, 20)
g3 = Wt_on_earth(1425, 280, 1025, 20)
g4 = Wt_on_earth(2480, 280, 920, 20)
# pipe
p1 = Pipe(450, 250, 30, 30)
p2 = Pipe(610, 230, 30, 50)
p3 = Pipe(735, 215, 30, 65)
p4 = Pipe(910, 215, 30, 65)
p5 = Pipe(2610, 250, 30, 30)
p6 = Pipe(2865, 250, 30, 30)
# stair
s11 = Stair(2145, 265, 15, 15)
s12 = Stair(2160, 250, 15, 30)
s13 = Stair(2175, 235, 15, 45)
s14 = Stair(2190, 220, 15, 60)

s21 = Stair(2240, 220, 15, 60)
s22 = Stair(2255, 235, 15, 45)
s23 = Stair(2270, 250, 15, 30)
s24 = Stair(2285, 265, 15, 15)

s31 = Stair(2375, 265, 15, 15)
s32 = Stair(2390, 250, 15, 30)
s33 = Stair(2405, 235, 15, 45)
s34 = Stair(2420, 220, 15, 60)
s35 = Stair(2435, 220, 15, 60)

s41 = Stair(2480, 220, 15, 60)
s42 = Stair(2495, 235, 15, 45)
s43 = Stair(2510, 250, 15, 30)
s44 = Stair(2525, 265, 15, 15)

s51 = Stair(2895, 265, 15, 15)
s52 = Stair(2910, 250, 15, 30)
s53 = Stair(2925, 235, 15, 45)
s54 = Stair(2940, 220, 15, 60)
s55 = Stair(2955, 205, 15, 75)
s56 = Stair(2970, 190, 15, 90)
s57 = Stair(2985, 175, 15, 105)
s58 = Stair(3000, 160, 15, 120)
s59 = Stair(3015, 160, 15, 120)
s60 = end_point(3120, 265)
# Question mark block
q1 = Qmark(255, 215)
q2 = Qmark(335, 215)  #
q3 = Qmark(350, 150)
q4 = Qmark(365, 215)
q5 = Qmark(1250, 215)  #
q6 = Qmark(1500, 150)
q7 = Qmark(1695, 215)
q8 = Qmark(1745, 215)
q9 = Qmark(1790, 215)
q10 = Qmark(1745, 150)  #
q11 = Qmark(2055, 150)
q12 = Qmark(2070, 150)
q13 = Qmark(2720, 215)
# hidden
h1 = hidden(1025, 200)
h2 = hidden(1615, 215)
# Brick
b1 = Brick(320, 215)
b2 = Brick(350, 215)
b3 = Brick(380, 215)
b4 = Brick(1235, 215)
b5 = Brick(1265, 215)
b6 = Brick(1280, 1505)
b7 = Brick(1295, 150)
b8 = Brick(1310, 150)
b9 = Brick(1325, 150)
b10 = Brick(1340, 150)
b11 = Brick(1355, 150)
b12 = Brick(1370, 150)
b13 = Brick(1385, 150)
b14 = Brick(1455, 150)
b15 = Brick(1470, 150)
b16 = Brick(1485, 150)
b17 = Brick(1500, 215)
b18 = Brick(1600, 215)
b19 = Brick(1890, 215)
b20 = Brick(1935, 150)
b21 = Brick(1950, 150)
b22 = Brick(1965, 150)
b23 = Brick(2040, 150)
b24 = Brick(2055, 215)
b25 = Brick(2070, 215)
b26 = Brick(2085, 150)
b27 = Brick(2690, 215)
b28 = Brick(2705, 215)
b29 = Brick(2735, 215)


map = [g1, g2, g3, g4,
       p1, p2, p3, p4, p5, p6,
       s11, s12, s13, s14,
       s21, s22, s23, s24,
       s31, s32, s33, s34, s35,
       s41, s42, s43, s44,
       s51, s52, s53, s54, s55, s56, s57, s58, s59,
       s60]

map_breakable = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13,
                 h1, h2,
                 b1, b2, b3, b4, b5, b6, b7, b8, b9, b10,
                 b11, b12, b13, b14, b15, b16, b17, b18, b19, b20,
                 b21, b22, b23, b24, b25, b26, b27, b28, b29]
