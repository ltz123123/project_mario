import pygame as pg
from character import *
from earth import *


def draw(map, map_q, mario, screen):
    for i in map:
        i.draw(mario, screen)
    for j in map_q:
        j.draw(mario, screen)


def colli(who, map, map_q):
    for i in map:
        if who.hitbox().colliderect(i.block()):
            return True
    for j in map_q:
        if who.hitbox().colliderect(j.block()):
            return True
    return False


def isEarth(who, map, map_q):
    for i in map:
        if who.hitbox().colliderect(i.earth()):
            return True
    for j in map_q:
        if who.hitbox().colliderect(j.earth()):
            return True
    return False


def hit_ceiling_hitbox():
    for i in map_breakable:
        if mario.head().colliderect(i.ceiling_hitbox()):
            i.broken = True
            return True


def hit_ceiling():
    for i in map_breakable:
        if mario.hitbox().colliderect(i.ceiling()):
            return True
    return False


def gravity(who):
    who.y += who.dy
    if hit_ceiling():
        who.dy = 3
    else:
        while colli(who, map, map_breakable):
            who.jumping = False
            who.y -= 1
    if not isEarth(who, map, map_breakable):
        if who.dy < 15:
            who.dy += 1
    else:
        while colli(who, map, map_breakable):
            who.jumping = False
            who.dy = 0
            who.y -= 1


def camera(sign):
    global moveCam
    if mario.x > 200:
        moveCam = True
    elif map[0].x > -5 or map[3].x < -1985:
        moveCam = False
    if moveCam:
        for i in map:
            i.x += mario.vel * sign
        for j in map_breakable:
            j.x += mario.vel * sign
        mario.x += mario.vel * sign
        m1.x += mario.vel * sign


def auto_run():
    def touch_pipe():
        for i in [p1, p2, p3, p4, p5, p6, s11]:
            if m1.hitbox().colliderect(i.block()):
                return True

    if touch_pipe():
        m1.y += 1
        if m1.left:
            m1.x += m1.vel
            m1.left = False
            m1.right = True
        elif m1.right:
            m1.x -= m1.vel
            m1.right = False
            m1.left = True
    if m1.left:
        m1.x -= m1.vel
    elif m1.right:
        m1.x += m1.vel
    if not isEarth(m1, map, map_breakable):
        if m1.dy < 15:
            m1.dy += 1
        m1.y += m1.dy
        m1.jumping = True
    else:
        m1.dy = 0
        m1.jumping = False


pg.init()
screen = pg.display.set_mode((500, 300))
pg.display.set_caption('Mario')
clock = pg.time.Clock()
marioImg = [pg.image.load('1.png'), pg.image.load('2.png'), pg.image.load('3.png'), pg.image.load('4.png'),
            pg.image.load('man.png')]
mario = character(50, 260, marioImg)
moveCam = False

# test auto_run
m1 = enemy(350, 135, None)

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
    draw(map, map_breakable, mario, screen)
    mario.draw(screen)
    m1.draw(screen)
    auto_run()
    gravity(mario)
    hit_ceiling_hitbox()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and mario.x > 0:
        mario.x -= mario.vel
        camera(1)
        mario.left = True
        mario.right = False
        if colli(mario, map, map_breakable):
            camera(-1)
            mario.x += mario.vel
    elif keys[pg.K_RIGHT]:
        mario.x += mario.vel
        camera(-1)
        mario.right = True
        mario.left = False
        if colli(mario, map, map_breakable):
            camera(1)
            mario.x -= mario.vel
    else:
        mario.left = False
        mario.right = False

    if isEarth(mario, map, map_breakable):
        if keys[pg.K_UP]:
            if not mario.jumping:
                mario.jumping = True
                mario.jump()

    pg.display.update()
pg.quit()
