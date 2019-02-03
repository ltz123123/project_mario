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

def gravity():
    if not(isEarth(map) or mario.jumping):
        mario.y += 5

def new_gravity():
    if not(isEarth(map) or mario.jumping):
        mario.dy += 1
        mario.y += mario.dy

map = map1_1()

pg.init()
screen = pg.display.set_mode((500,300))
pg.display.set_caption('Mario')
clock = pg.time.Clock()
moveCam = False

mario = character(50,260)

run = True
while run:
    clock.tick(30)
    print mario.x,mario.y

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False


    screen.fill((0, 0, 0))
    draw(map,mario,screen)
    gravity()
    mario.draw(screen)


    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and mario.x > 0:
        mario.x -= mario.vel

        if colli(map):
            mario.x += mario.vel
    if keys[pg.K_RIGHT] and mario.x < 9750:
        mario.x += mario.vel

        if colli(map):
            mario.x -= mario.vel

    if not(mario.jumping):
        if keys[pg.K_UP] and isEarth(map):
            mario.jumping = True
    else:
        mario.jump(colli,map)

    pg.display.update()
pg.quit()
