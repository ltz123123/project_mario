import pygame as pg
from character import character
from earth import *
from stage1_1 import *



def draw(map, map_q, mario, screen):
    for keys, values in map.items():
        wt_on_earth(values).draw(mario, screen)
    for i in range(len(map_q)):
        map_q[i].draw(mario, screen)



def colli(map, map_q):
    for keys, values in map.items():
        if mario.hitbox().colliderect(wt_on_earth(values).block()):
            return True
    for i in range(len(map_q)):
        if mario.hitbox().colliderect(map_q[i].block()):
            return True
    return False

def isEarth(map, map_q):
    for keys, values in map.items():
        if mario.hitbox().colliderect(wt_on_earth(values).earth()):
            return True
    for i in range(len(map_q)):
        if mario.hitbox().colliderect(map_q[i].earth()):
            return True
    return False

def breaking(map_q):
    for i in range(len(map_q)):
        if mario.hitbox().colliderect(map_q[i].ceiling()):
            mario.jumping = False
            map_q[i].broken = True

def vert_move():
    mario.y += mario.dy
    while colli(map, map_qmark):
        mario.jumping = False
        mario.y -= 1


def gravity():
    if not isEarth(map, map_qmark):
        mario.dy += 3


def reset():
    if mario.y > 300:
        mario.x = 50
        mario.y = 260


map = map1_1()


pg.init()
screen = pg.display.set_mode((500, 300))
pg.display.set_caption('Mario')
clock = pg.time.Clock()
mario = character(50, 260)

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
    breaking(map_qmark)
    reset()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and mario.x > 0:
        mario.x -= mario.vel
        if colli(map, map_qmark):
            mario.x += mario.vel

    if keys[pg.K_RIGHT]:
        mario.x += mario.vel
        if colli(map, map_qmark):
            mario.x -= mario.vel

    if isEarth(map, map_qmark):
        if keys[pg.K_UP]:
            if not mario.jumping:
                mario.jumping = True
                mario.jump()

    pg.display.update()
pg.quit()
