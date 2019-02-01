import pygame as pg

class character:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 40
        self.vel = 5
        self.jumping = False
        self.jumpCount = 10
    def hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)
    def jump(self):
        if self.jumpCount >= -10:
            if self.jumpCount > 0:
                self.y -= 10
                if colli():
                    self.y += 10
                    self.jumping = False
                    self.jumpCount = 10
            else:
                self.y += 10
                if colli():
                    self.y -= 10
                    self.jumping = False
                    self.jumpCount = 10
            self.jumpCount -= 1
        else:
            self.jumping = False
            self.jumpCount = 10
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

def draw():
    pg.draw.rect(screen,(0,255,0),(b1.x,b1.y,b1.width,b1.height))
    pg.draw.rect(screen,(0,255,0),(b2.x,b2.y,b2.width,b2.height))

def colli():
    if mario.hitbox().colliderect(b1.block()) or mario.hitbox().colliderect(b2.block()):
        return True
    return False
def isEarth():
    if mario.hitbox().colliderect(b1.earth()) or mario.hitbox().colliderect(b2.earth()):
        return True
def gravity():
    if not(isEarth() or mario.jumping):
        mario.y += 10

def camera(sign):
    global moveCam
    if mario.x > 200:
        moveCam = True
    if moveCam:
        b1.x += mario.vel * sign
        b2.x += mario.vel * sign
        mario.x += mario.vel * sign

pg.init()
screen = pg.display.set_mode((600,400))
pg.display.set_caption('Mario')
clock = pg.time.Clock()
moveCam = False

mario = character(50,320)
b1 = wt_on_earth(0,360,400,40)
b2 = wt_on_earth(400,320,200,80)

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