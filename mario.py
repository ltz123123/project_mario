import pygame as pg
from character import *
from earth import *


def draw(map, map_q, mario, screen):
    for i in map:
        i.draw(mario, screen)
    for j in map_q:
        j.draw(mario, screen)
    for k in all_enemy:
        k.draw(screen)


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


def gravity(mario):
    mario.y += mario.dy

    if hit_ceiling():
        mario.dy = 3
    else:
        while colli(mario, map, map_breakable):
            mario.jumping = False
            mario.y -= 1

    if not isEarth(mario, map, map_breakable):
        if mario.dy < 15:
            mario.dy += 1
        mario.jumping = True
    else:
        while colli(mario, map, map_breakable):
            mario.jumping = False
            mario.dy = 0
            mario.y -= 1


def camera(sign):
    global moveCam
    if mario.x > 195:
        moveCam = True
    elif map[0].x > -5:
        moveCam = False
    if moveCam:
        for i in map:
            i.x += mario.vel * sign
        for j in map_breakable:
            j.x += mario.vel * sign
        for k in all_enemy:
            k.x += mario.vel * sign
        mario.x += mario.vel * sign


def auto_run():
    def touch_pipe(q):
        for i in [p1, p2, p3, p4, p5, p6, s11]:
            if q.hitbox().colliderect(i.block()):
                return True

    for j in all_enemy:
        if (j.x - mario.x) < 300:
            j.spawned = True
        if j.lp >= 0:
            if j.y > 300:
                j.lp -= 1
            j.run()
            if touch_pipe(j):
                if j.left:
                    j.left = False
                    j.right = True
                elif j.right:
                    j.right = False
                    j.left = True
            if not isEarth(j, map, map_breakable):
                j.y += 5


def hit_enemy():
    for i in all_enemy:
        if mario.hitbox().colliderect(i.hitbox()) and mario.y < i.y - 5:
            i.hit_once()
            mario.jumping = True
            mario.dy = -7


pg.init()
screen = pg.display.set_mode((500, 300))
pg.display.set_caption('Mario')
clock = pg.time.Clock()
marioImg_s = [pg.image.load('stand.png'), pg.image.load('jl.png'), pg.image.load('jr.png')]
marioImg_l = [pg.image.load('L1.png'), pg.image.load('L2.png'), pg.image.load('L3.png'), pg.image.load('L4.png'),
              pg.image.load('L5.png')]
marioImg_r = [pg.image.load('R1.png'), pg.image.load('R2.png'), pg.image.load('R3.png'), pg.image.load('R4.png'),
              pg.image.load('R5.png')]
mario = character(50, 260, marioImg_s, marioImg_l, marioImg_r)
moveCam = False

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
    auto_run()
    hit_enemy()
    gravity(mario)
    hit_ceiling_hitbox()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and mario.x > 0:
        mario.x -= mario.vel
        camera(1)
        mario.left = True
        mario.right = False
        mario.standing = False
        if colli(mario, map, map_breakable):
            camera(-1)
            mario.x += mario.vel
    elif keys[pg.K_RIGHT]:
        mario.x += mario.vel
        camera(-1)
        mario.right = True
        mario.left = False
        mario.standing = False
        if colli(mario, map, map_breakable):
            camera(1)
            mario.x -= mario.vel
    else:
        mario.standing = True

    if isEarth(mario, map, map_breakable):
        if keys[pg.K_UP]:
            if not mario.jumping:
                mario.jumping = True
                mario.jump()

    pg.display.update()
pg.quit()
