import pygame as pg

class character:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 20
        self.vel = 4
        self.jumping = False
        self.jumpspeed = 5
        self.jc = 16
        self.jumpCount = 16
    def hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)
    def jump(self):
        if self.jumpCount >= -self.jc:
            if self.jumpCount > 0:
                self.y -= self.jumpspeed
                if colli():
                    self.y += self.jumpspeed
                    self.jumping = False
                    self.jumpCount = self.jc
            else:
                self.y += self.jumpspeed
                if colli():
                    self.y -= self.jumpspeed
                    self.jumping = False
                    self.jumpCount = self.jc
            self.jumpCount -= 1
        else:
            self.jumping = False
            self.jumpCount = self.jc
    def draw(self):
        pg.draw.rect(screen,(255,255,255),self.hitbox())



class wt_on_earth:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def block(self):
        return pg.Rect(self.x,self.y,self.width,self.height)
    def earth(self):
        return pg.Rect(self.x,self.y - 4,self.width,4)
    def draw(self):
        if self.x - mario.x < 450:
            pg.draw.rect(screen, (0, 255, 0), (self.x,self.y,self.width,self.height))

def draw():
    for i in range(len(map)):
        map[i].draw()

def colli():
    for i in range(len(map)):
        if mario.hitbox().colliderect(map[i].block()):
            return True
    return False
def isEarth():
    for i in range(len(map)):
        if mario.hitbox().colliderect(map[i].earth()):
            return True
    return False
def gravity():
    if not(isEarth() or mario.jumping):
        mario.y += 5

def camera(sign):
    global moveCam
    if 200 < mario.x < 3200:
        moveCam = True
    if moveCam:
        for i in range(len(map)):
            map[i].x += mario.vel * sign
        mario.x += mario.vel * sign

pg.init()
screen = pg.display.set_mode((500,300))
pg.display.set_caption('Mario')
clock = pg.time.Clock()
moveCam = False

mario = character(50,260)
#groung
g1 = wt_on_earth(0,280,1100,20)
g2 = wt_on_earth(1135,280,240,20)
g3 = wt_on_earth(1425,280,1025,20)
g4 = wt_on_earth(2480,280,820,20)
#pipe
p1 = wt_on_earth(450,250,30,30)
p2 = wt_on_earth(610,230,30,50)
p3 = wt_on_earth(735,215,30,65)
p4 = wt_on_earth(910,215,30,65)
p5 = wt_on_earth(2610,250,30,30)
p6 = wt_on_earth(2865,250,30,30)
#stair
s11 = wt_on_earth(2145,265,15,15)
s12 = wt_on_earth(2160,250,15,30)
s13 = wt_on_earth(2175,235,15,45)
s14 = wt_on_earth(2190,220,15,60)

s21 = wt_on_earth(2240,220,15,60)
s22 = wt_on_earth(2255,235,15,45)
s23 = wt_on_earth(2270,250,15,30)
s24 = wt_on_earth(2285,265,15,15)

s31 = wt_on_earth(2375,265,15,15)
s32 = wt_on_earth(2390,250,15,30)
s33 = wt_on_earth(2405,235,15,45)
s34 = wt_on_earth(2420,220,15,60)
s35 = wt_on_earth(2435,220,15,60)

s41 = wt_on_earth(2480,220,15,60)
s42 = wt_on_earth(2495,235,15,45)
s43 = wt_on_earth(2510,250,15,30)
s44 = wt_on_earth(2525,265,15,15)

s51 = wt_on_earth(2895,265,15,15)
s52 = wt_on_earth(2910,250,15,30)
s53 = wt_on_earth(2925,235,15,45)
s54 = wt_on_earth(2940,220,15,60)
s55 = wt_on_earth(2955,205,15,75)
s56 = wt_on_earth(2970,190,15,90)
s57 = wt_on_earth(2985,175,15,105)
s58 = wt_on_earth(3000,160,15,120)
s59 = wt_on_earth(3015,160,15,120)


map = [g1,g2,g3,g4,
       p1,p2,p3,p4,p5,p6,
       s11,s12,s13,s14,
       s21,s22,s23,s24,
       s31,s32,s33,s34,s35,
       s41,s42,s43,s44,
       s51,s52,s53,s54,s55,s56,s57,s58,s59]

run = True
while run:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False

    screen.fill((0, 0, 0))
    draw()
    gravity()
    mario.draw()


    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and mario.x > 0:
        mario.x -= mario.vel
        camera(1)
        if colli():
            camera(-1)
            mario.x += mario.vel
    if keys[pg.K_RIGHT] and mario.x < 975:
        mario.x += mario.vel
        camera(-1)
        if colli():
            camera(1)
            mario.x -= mario.vel
    if not(mario.jumping):
        if keys[pg.K_UP] and isEarth():
            mario.jumping = True
    else:
        mario.jump()

    pg.display.update()
pg.quit()