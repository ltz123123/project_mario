import pygame as pg

class character:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 20
        self.vel = 5
        self.jumping = False
        self.jc = 15
        self.jumpCount = 15
    def hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)
    def jump(self):
        if self.jumpCount >= -self.jc:
            if self.jumpCount > 0:
                self.y -= 10
                if colli():
                    self.y += 10
                    self.jumping = False
                    self.jumpCount = self.jc
            else:
                self.y += 10
                if colli():
                    self.y -= 10
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
        return pg.Rect(self.x,self.y -5,self.width,5)
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
        mario.y += 10

def camera(sign):
    global moveCam
    if 200 < mario.x < 3200:
        moveCam = True
    if moveCam:
        for i in range(len(map)):
            map[i].x += mario.vel * sign
        mario.x += mario.vel * sign

pg.init()
screen = pg.display.set_mode((600,300))
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
p1 = wt_on_earth(450,240,30,40)
p2 = wt_on_earth(610,210,30,80)
p3 = wt_on_earth(735,180,30,120)
p4 = wt_on_earth(910,180,30,120)
#stair
s11 = wt_on_earth(2145,260,15,20)
s12 = wt_on_earth(2160,240,15,40)
s13 = wt_on_earth(2175,220,15,60)
s14 = wt_on_earth(2190,200,15,80)
map = [g1,g2,g3,g4,
       p1,p2,p3,p4,
       s11,s12,s13,s14]

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