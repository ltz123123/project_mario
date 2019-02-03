import pygame as pg
from character import character
import earth
from stage1_1 import map1_1

def draw(map,mario,screen):
    for keys,values in map.items():
        earth.wt_on_earth(values).draw(mario,screen)

def colli(map):
    for keys,values in map.items():
        if mario.hitbox().colliderect(earth.wt_on_earth(values).block()):
            return True
    return False

def isEarth(map):
    for keys,values in map.items():
        if mario.hitbox().colliderect(earth.wt_on_earth(values).earth()):
            return True
    return False

def vert_move():
    mario.y += mario.dy
    while colli(map):
        mario.jumping = False
        mario.y -= 1

def gravity():
    if not isEarth(map):
        mario.dy += 3

map = map1_1()

pg.init()
screen = pg.display.set_mode((500,300))
pg.display.set_caption('Mario')
clock = pg.time.Clock()
mario = character(50,260)

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
    draw(map,mario,screen)
    mario.draw(screen)
    vert_move()
    gravity()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and mario.x > 0:
        mario.x -= mario.vel
        if colli(map):
            mario.x += mario.vel

    if keys[pg.K_RIGHT] and mario.x < 9750:
        mario.x += mario.vel
        if colli(map):
            mario.x -= mario.vel

    if isEarth(map):
        if keys[pg.K_UP]:
            if not(mario.jumping):
                mario.jumping = True
                mario.jump()

    pg.display.update()
pg.quit()
