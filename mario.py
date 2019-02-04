import pygame as pg
from character import character
from earth import *


def draw(map, map_q, mario, screen):
    for i in map:
        i.draw(mario, screen)
    for j in map_q:
        j.draw(mario, screen)


def colli(map, map_q):
    for i in map:
        if mario.hitbox().colliderect(i.block()):
            return True
    for j in map_q:
        if mario.hitbox().colliderect(j.block()):
            return True
    return False


def isEarth(map, map_q):
    for i in map:
        if mario.hitbox().colliderect(i.earth()):
            return True
    for j in map_q:
        if mario.hitbox().colliderect(j.earth()):
            return True
    return False


def hit_ceiling_hitbox():
    for i in map_qmark:
        if mario.head().colliderect(i.ceiling_hitbox()):
            i.broken = True
            return True
def hit_ceiling():
    for i in map_qmark:
        if mario.hitbox().colliderect(i.ceiling()):
            return True
    return False

def vert_move():
    mario.y += mario.dy
    if hit_ceiling():
        mario.dy = 0
    else:
        while colli(map, map_qmark):
            mario.jumping = False
            mario.y -= 1


def gravity():
    if not isEarth(map, map_qmark):
        mario.dy += 2
    else:
        while colli(map, map_qmark):
            mario.jumping = False
            mario.y -= 1


def camera(sign):
    global moveCam
    if mario.x > 200:
        moveCam = True
    if moveCam:
        for i in map:
            i.x += mario.vel * sign
        for j in map_qmark:
            j.x += mario.vel * sign
        mario.x += mario.vel * sign


pg.init()
screen = pg.display.set_mode((500, 300))
pg.display.set_caption('Mario')
clock = pg.time.Clock()
mario = character(50, 260)
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
    draw(map, map_qmark, mario, screen)
    mario.draw(screen)
    vert_move()
    gravity()
    hit_ceiling_hitbox()
    print(mario.dy)

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and mario.x > 0:
        mario.x -= mario.vel
        camera(1)
        if colli(map, map_qmark):
            camera(-1)
            mario.x += mario.vel

    if keys[pg.K_RIGHT]:
        mario.x += mario.vel
        camera(-1)
        if colli(map, map_qmark):
            camera(1)
            mario.x -= mario.vel

    if isEarth(map, map_qmark):
        if keys[pg.K_UP]:
            if not mario.jumping:
                mario.jumping = True
                mario.jump()

    pg.display.update()
pg.quit()
