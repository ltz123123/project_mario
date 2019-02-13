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
        return pg.Rect(self.x - 4, self.y - 4, self.width + 8, 4)

    def draw(self, mario, screen):
        if abs(self.x - mario.x) < 1300:
            pg.draw.rect(screen, (47, 79, 79), (self.x, self.y, self.width, self.height))


class Qmark(Wt_on_earth):
    def __init__(self, x, y, width, height):
        Wt_on_earth.__init__(self, x, y, width, height)
        self.broken = False
        self.bonus = bonus

    def bonus_hit_box(self):
        pass

    def take_bonus(self):
        pass



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


class Brick(Wt_on_earth):
    def __init__(self, x, y, width, height):
        Wt_on_earth.__init__(self, x, y, width, height)
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


# ground
g1 = Wt_on_earth(0, 280, 1100, 20)
g2 = Wt_on_earth(1135, 280, 240, 20)
g3 = Wt_on_earth(1425, 280, 1025, 20)
g4 = Wt_on_earth(2480, 280, 820, 20)
# pipe
p1 = Wt_on_earth(450, 250, 30, 30)
p2 = Wt_on_earth(610, 230, 30, 50)
p3 = Wt_on_earth(735, 215, 30, 65)
p4 = Wt_on_earth(910, 215, 30, 65)
p5 = Wt_on_earth(2610, 250, 30, 30)
p6 = Wt_on_earth(2865, 250, 30, 30)
# stair
s11 = Wt_on_earth(2145, 265, 15, 15)
s12 = Wt_on_earth(2160, 250, 15, 30)
s13 = Wt_on_earth(2175, 235, 15, 45)
s14 = Wt_on_earth(2190, 220, 15, 60)

s21 = Wt_on_earth(2240, 220, 15, 60)
s22 = Wt_on_earth(2255, 235, 15, 45)
s23 = Wt_on_earth(2270, 250, 15, 30)
s24 = Wt_on_earth(2285, 265, 15, 15)

s31 = Wt_on_earth(2375, 265, 15, 15)
s32 = Wt_on_earth(2390, 250, 15, 30)
s33 = Wt_on_earth(2405, 235, 15, 45)
s34 = Wt_on_earth(2420, 220, 15, 60)
s35 = Wt_on_earth(2435, 220, 15, 60)

s41 = Wt_on_earth(2480, 220, 15, 60)
s42 = Wt_on_earth(2495, 235, 15, 45)
s43 = Wt_on_earth(2510, 250, 15, 30)
s44 = Wt_on_earth(2525, 265, 15, 15)

s51 = Wt_on_earth(2895, 265, 15, 15)
s52 = Wt_on_earth(2910, 250, 15, 30)
s53 = Wt_on_earth(2925, 235, 15, 45)
s54 = Wt_on_earth(2940, 220, 15, 60)
s55 = Wt_on_earth(2955, 205, 15, 75)
s56 = Wt_on_earth(2970, 190, 15, 90)
s57 = Wt_on_earth(2985, 175, 15, 105)
s58 = Wt_on_earth(3000, 160, 15, 120)
s59 = Wt_on_earth(3015, 160, 15, 120)
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
# Brick
b1 = Brick(320, 215, 15, 15)
b2 = Brick(350, 215, 15, 15)
b3 = Brick(380, 215, 15, 15)
b4 = Brick(1235, 215, 15, 15)
b5 = Brick(1265, 215, 15, 15)
b6 = Brick(1280, 150, 15, 15)
b7 = Brick(1295, 150, 15, 15)
b8 = Brick(1310, 150, 15, 15)
b9 = Brick(1325, 150, 15, 15)
b10 = Brick(1340, 150, 15, 15)
b11 = Brick(1355, 150, 15, 15)
b12 = Brick(1370, 150, 15, 15)
b13 = Brick(1385, 150, 15, 15)
b14 = Brick(1455, 150, 15, 15)
b15 = Brick(1470, 150, 15, 15)
b16 = Brick(1485, 150, 15, 15)
b17 = Brick(1500, 215, 15, 15)
b18 = Brick(1600, 215, 15, 15)
b19 = Brick(1890, 215, 15, 15)
b20 = Brick(1935, 150, 15, 15)
b21 = Brick(1950, 150, 15, 15)
b22 = Brick(1965, 150, 15, 15)
b23 = Brick(2050, 150, 15, 15)
b24 = Brick(2065, 215, 15, 15)
b25 = Brick(2080, 215, 15, 15)
b26 = Brick(2095, 150, 15, 15)
b27 = Brick(2690, 215, 15, 15)
b28 = Brick(2705, 215, 15, 15)
b29 = Brick(2735, 215, 15, 15)

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
                 b21, b22, b23, b24, b25, b26, b27, b28, b29]
