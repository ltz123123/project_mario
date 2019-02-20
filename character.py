import pygame as pg


class character(object):
    def __init__(self, x, y):
        self.life = 3
        self.big = False
        self.shooting = True
        self.immortal = False
        self.x = x
        self.y = y
        self.width = 10
        self.height = 20
        self.vel = 5
        self.wall_left = False
        self.wall_right = False
        self.dy = 0
        self.jumping = False
        self.left = False
        self.right = True
        self.standing = True
        self.walk_tick = 0
        self.img_s = None
        self.img_l = None
        self.img_r = None

    def jump(self):
        self.jumping = True
        self.dy = -12

    def head(self):
        return pg.Rect(self.x, self.y, self.width, self.height * 0.2)

    def hitbox(self):
        return pg.Rect(self.x + 2, self.y, self.width - 2, self.height)

    def left_hitbox(self):
        return pg.Rect(self.x - 1, self.y, self.width, self.height)

    def right_hitbox(self):
        return pg.Rect(self.x + 1, self.y, self.width, self.height)

    def draw(self, window):
        if self.walk_tick + 1 > 25:
            self.walk_tick = 0
        if not self.jumping:
            if self.standing:
                window.blit(self.img_s[0], (self.x, self.y))
            elif self.left:
                window.blit(self.img_l[self.walk_tick // 10], (self.x, self.y))
                self.walk_tick += 1
            else:
                window.blit(self.img_r[self.walk_tick // 10], (self.x, self.y))
                self.walk_tick += 1
        elif self.jumping:
            if self.left:
                window.blit(self.img_s[1], (self.x, self.y))
            elif self.right:
                window.blit(self.img_s[2], (self.x, self.y))
        if self.immortal:
            pg.draw.circle(window, (255, 255, 255), (self.x + self.width // 2, self.y + self.height // 2), self.width * 2, 1)
        if self.shooting:
            pg.draw.circle(window, (255, 0, 0), (self.x + self.width // 2, self.y + self.width // 3), self.width // 2 - 2)

    def get_big(self):
        if not self.big:
            self.height, self.width = 30, 20
            self.big = True
            self.y -= 10
            self.load_big()
        elif self.big:
            self.height, self.width = 20, 10
            self.y += 10
            self.big = False
            self.load()

    def can_shoot(self):
        if not self.shooting:
            self.shooting = True
        elif self.shooting:
            self.shooting = False

    def dont_die(self):
        if not self.immortal:
            self.immortal = True
        elif self.immortal:
            self.immortal = False

    def load(self):
        dest = 'normal'
        self.img_s = [pg.image.load(dest + '/stand.png'), pg.image.load(dest + '/jl.png'),
                      pg.image.load(dest + '/jr.png')]
        self.img_l = [pg.image.load(dest + '/L' + str(x + 1) + '.png') for x in range(5)]
        self.img_r = [pg.image.load(dest + '/R' + str(x + 1) + '.png') for x in range(5)]

    def load_big(self):
        for i in range(3):
            self.img_s[i] = pg.transform.scale(self.img_s[i], [20, 30])
        for j in range(5):
            self.img_l[j] = pg.transform.scale(self.img_l[j], [20, 30])
        for k in range(5):
            self.img_r[k] = pg.transform.scale(self.img_r[k], [20, 30])


class enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15
        self.vel = 1.3
        self.left = True
        self.right = False
        self.dy = 0
        self.spawned = False
        self.lp = 1
        self.color = (0, 255, 255)
        self.walkCount = 0
    def run(self):
        if self.lp > 0:
            if self.left:
                self.x -= self.vel
            elif self.right:
                self.x += self.vel

    def hit_once(self, q):
        self.lp -= 1

    def hitbox(self):
        if self.lp == 0:
            return pg.Rect(0, 0, 1, 1)
        elif self.spawned:
            return pg.Rect(self.x, self.y, self.width, self.height)
        return pg.Rect(0, 0, 1, 1)

    def draw(self, ma, window):
        if self.walkCount + 1 > 20:
            self.walkCount = 0
        if abs(self.x - ma.x) < 1300 and self.spawned and self.lp > 0:
            if self.left:
                window.blit(mush_img[0][self.walkCount // 10], (self.x, self.y))
            if self.right:
                window.blit(mush_img[1][self.walkCount // 10], (self.x, self.y))
            self.walkCount += 1


class enemy2(enemy):
    def __init__(self, x, y):
        enemy.__init__(self, x, y)
        self.height = 20
        self.width = 15
        self.lp = 3
        self.img_sl = pg.image.load('turtle/sl.png')
        self.img_l = [pg.image.load('turtle/l1.png'), pg.image.load('turtle/l2.png')]
        self.img_r = [pg.image.load('turtle/r1.png'), pg.image.load('turtle/r2.png')]
    def hit_once(self, q):
        if self.lp == 3:
            self.height = 15
            self.width = 15
            self.y += 5
            self.vel = 0
        elif self.lp == 2:
            self.vel = 6
            self.left = q.left
            self.right = q.right
        self.lp -= 1

    def draw(self, ma, window):
        if self.walkCount + 1 > 20:
            self.walkCount = 0
        if abs(self.x - ma.x) < 1300 and self.spawned and self.lp > 0:
            if self.lp == 3:
                if self.left:
                    window.blit(self.img_l[self.walkCount // 10], (self.x, self.y))
                if self.right:
                    window.blit(self.img_r[self.walkCount // 10], (self.x, self.y))
                self.walkCount += 1
            elif self.lp < 3:
                window.blit(self.img_sl, (self.x, self.y))


class bonus(enemy):
    def __init__(self, x, y, l, r, which_type):
        enemy.__init__(self, x, y)
        self.vel = 2
        self.right = r
        self.left = l
        self.spawn_delay = 15
        self.color = (0, 255, 200)
        self.which_type = which_type
        self.dy = 0

    def run(self):
        if self.spawn_delay > 0:
            self.spawn_delay -= 1
        elif self.spawn_delay == 0:
            if self.spawned and self.lp > 0:
                if self.left:
                    self.x -= self.vel
                elif self.right:
                    self.x += self.vel

    def took(self, a):
        if self.which_type == 1:
            if not a.big:
                a.get_big()
        elif self.which_type == 2:
            a.can_shoot()
        elif self.which_type == 3:
            a.dont_die()

    def draw(self, mario, window):
        if self.spawned and self.lp > 0:
            if self.which_type == 1:
                if self.left:
                    window.blit(big_mush_img[0], (self.x, self.y))
                elif self.right:
                    window.blit(big_mush_img[1], (self.x, self.y))
            elif self.which_type == 2:
                window.blit(flower_img, (self.x - 5, self.y - 5))
            elif self.which_type == 3:
                window.blit(star_img, (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, left, right):
        self.x = x
        self.y = y
        self.left = left
        self.right = right
        self.vel = 8
        self.radius = 5
        self.dy = -5

    def run(self):
        if self.left:
            self.x -= self.vel
        elif self.right:
            self.x += self.vel

    def fake_hitbox(self):
        return pg.Rect(self.x - 5, self.y - 10, 10, 20)

    def hitbox(self):
        return pg.Rect(self.x - 5, self.y - 5, 10, 10)

    def draw(self, empty, window):
        pg.draw.circle(window, (255, 255, 255), (self.x, self.y), self.radius)


mario = character(50, 260)
mush_img = [[pg.image.load('mush/l1.png'), pg.image.load('mush/l2.png')],
        [pg.image.load('mush/r1.png'), pg.image.load('mush/r2.png')]]
big_mush_img = [pg.image.load('bonus/big_l.png'), pg.image.load('bonus/big_r.png')]
flower_img = pg.transform.scale(pg.image.load('bonus/flower.png'), [20, 20])
star_img = pg.image.load('bonus/star.png')
m1 = enemy(435, 265)
m2 = enemy(715, 265)
m3 = enemy(870, 265)
m4 = enemy(895, 265)
m5 = enemy(1360, 135)
m6 = enemy(1385, 135)
m7 = enemy(1620, 265)
m8 = enemy(1640, 265)
m9 = enemy(2065, 265)
m10 = enemy(2085, 265)
m11 = enemy(2110, 265)
m12 = enemy(2130, 265)
m13 = enemy(2820, 265)
m14 = enemy(2840, 265)
t1 = enemy2(1790, 260)
# 1 = big mush, 2 = flower, 3 = star
bonus1 = bonus(335, 200, False, True, 1)
bonus2 = bonus(1745, 135, False, True, 1)
bonus3 = bonus(1025, 185, False, True, 1)
bonus4 = bonus(1250, 200, False, False, 2)
bonus5 = bonus(1615, 200, False, True, 3)

all_enemy = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, t1]
all_bonus = [bonus1, bonus2, bonus3, bonus4, bonus5]
bullet = []
