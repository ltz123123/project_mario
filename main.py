from character import *
from earth import *


def draw():
    screen.fill((0, 0, 0))
    for i in bullet + map + map_breakable + all_enemy + all_bonus:
        i.draw(mario, screen)
    mario.draw(screen)


def collision(who):
    for i in map + map_breakable:
        if who.colliderect(i.block()):
            return True
    return False


def left_colli():
    for i in map + map_breakable:
        if mario.left_hitbox().colliderect(i.block()):
            return True
    return False


def right_colli():
    for i in map + map_breakable:
        if mario.right_hitbox().colliderect(i.block()):
            return True
    return False


def is_earth(who):
    for i in map + map_breakable:
        if who.colliderect(i.earth()):
            return True
    return False


def camera(sign):
    global move_cam, cam_ref
    if 0 < cam_ref < 3100:
        cam_ref -= mario.vel * sign
    if 240 < cam_ref < 3095:
        move_cam = True
    else:
        move_cam = False
    if move_cam:
        for i in bullet + map + map_breakable + all_enemy + all_bonus:
            i.x += mario.vel * sign


def auto_run():
    def touch_pipe(q):
        for i in [p1, p2, p3, p4, p5, p6, s11]:
            if q.hitbox().colliderect(i.block()):
                return True

    for k in [m1, m2, m3, m5, m7, m9, m13, t1]:
        if (k.x - mario.x) < 250:
            k.spawned = True
        m4.spawned = m3.spawned
        m6.spawned = m5.spawned
        m8.spawned = m7.spawned
        m10.spawned = m9.spawned
        m11.spawned = m9.spawned
        m12.spawned = m9.spawned
        m14.spawned = m13.spawned

    for j in all_enemy + all_bonus:
        if j.lp >= 0 and j.spawned:
            j.run()
            if j.y > 350:
                j.lp -= 1

            if touch_pipe(j):
                if j.left:
                    j.left = False
                    j.right = True
                elif j.right:
                    j.right = False
                    j.left = True
            if not is_earth(j.hitbox()):
                j.y += 5

    if bonus5.spawned and bonus5.lp >= 0:
        if bonus5.x > 500:
            bonus5.lp -= 1
        bonus5.y += bonus5.dy
        if not is_earth(bonus5.hitbox()):
            if bonus5.dy < 15:
                bonus5.dy += 1
        else:
            bonus5.dy = -13
            while collision(bonus5.hitbox()) and bonus5.dy >= 5:
                bonus5.dy = 0
                bonus5.y -= 1

    for j in bullet:
        if abs(j.x - mario.x) < 300:
            j.run()
        else:
            bullet.pop(bullet.index(j))
        if collision(j.hitbox()):
            bullet.pop(bullet.index(j))

        j.y += j.dy
        if is_earth(j.fake_hitbox()):
            j.dy = -5
        else:
            if j.dy < 5:
                j.dy += 2


def mario_movement():
    def hit_ceiling():
        for i in map_breakable:
            if mario.hitbox().colliderect(i.ceiling()):
                if mario.head().colliderect(i.ceiling_hitbox()):
                    i.broke(mario)
                return True
        return False

    mario.wall_left = left_colli()
    mario.wall_right = right_colli()

    if mario.jumping:
        mario.y += mario.dy
        if mario.dy < 0:
            hit_ceiling()

    if not is_earth(mario.hitbox()):
        if not goal:
            if mario.dy < 15:
                mario.dy += 1
        else:
            mario.dy = 0

        mario.jumping = True
    else:
        while collision(mario.hitbox()) and mario.dy >= 0:
            mario.jumping = False
            mario.dy = 0
            mario.y -= 1


def shoot():
    bullet.append(projectile(mario.x + mario.width // 2, mario.y + mario.height // 2, mario.left, mario.right))


def game_flow():
    def dead():
        global cam_ref, immortal_time
        immortal_time = 300
        mario.life -= 1
        mario.x, mario.y = 50, 260
        cam_ref = 50
        reset_value = map[0].x
        for i in map + map_breakable + all_enemy + all_bonus:
            i.x -= reset_value
        if mario.immortal:
            mario.immortal = False
        if mario.big:
            mario.get_big()
        if mario.shooting:
            mario.can_shoot()
        mario.load()

    def immortal_ticking():
        global immortal_time
        if immortal_time > 0:
            immortal_time -= 1
        else:
            mario.immortal = False
            immortal_time = 300

    for p in all_enemy:
        if mario.hitbox().colliderect(p.hitbox()):
            p.hit_once(mario)
            if not mario.immortal:
                if mario.jumping or mario.dy > 10:
                    mario.dy = -7
                elif mario.shooting:
                    mario.can_shoot()
                    p.lp = 0
                    pg.time.delay(1000)
                elif mario.big:
                    pg.time.delay(1000)
                    mario.get_big()
                    p.lp = 0
                else:
                    pg.time.delay(1000)
                    dead()
            elif mario.immortal:
                p.lp = 0
        for g in bullet:
            if g.hitbox().colliderect(p.hitbox()):
                p.lp = 0
                bullet.pop(bullet.index(g))

    if t1.lp == 1:
        for o in all_enemy[0:-1]:
            if t1.hitbox().colliderect(o.hitbox()):
                o.hit_once(None)
    for w in all_bonus:
        if mario.hitbox().colliderect(w.hitbox()):
            w.lp -= 1
            w.took(mario)

    if mario.immortal:
        immortal_ticking()

    if mario.y > 300:
        dead()
        mario.immortal = False

    if q2.broken:
        bonus1.spawned = True
    if q10.broken:
        bonus2.spawned = True
    if h1.broken:
        bonus3.spawned = True
    if q5.broken:
        bonus4.spawned = True
    if h2.broken:
        bonus5.spawned = True
        bonus5.vel = 5


def end():
    global cam_ref, goal

    def goal_animation():
        if not is_earth(mario.hitbox()):
            mario.y += 5
        if is_earth(mario.hitbox()) and not mario.hitbox().colliderect(s60.castle()):
            mario.x += 2
            mario.jumping = False
        elif mario.hitbox().colliderect(s60.castle()):
            mario.standing = True

    if mario.hitbox().colliderect(s60.pole()):
        goal = True
    if goal:
        goal_animation()


pg.init()
screen = pg.display.set_mode((500, 300))
pg.display.set_caption('scuffed Mario')
clock = pg.time.Clock()
goal = False
move_cam = False
cam_ref = 50
immortal_time = 300
mario.load()


run = True
while run:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
        if event.type == pg.KEYDOWN and not goal:
            if event.key == pg.K_SPACE and mario.shooting:
                shoot()

    draw()
    auto_run()
    mario_movement()
    game_flow()
    end()

    if not goal:
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and mario.x > 0:
            if not mario.wall_left:
                camera(1)
                if not move_cam:
                    mario.x -= mario.vel
                mario.left = True
                mario.right = False
                mario.standing = False
        elif keys[pg.K_RIGHT] and mario.x < 490:
            if not mario.wall_right:
                camera(-1)
                if not move_cam:
                    mario.x += mario.vel
                mario.right = True
                mario.left = False
                mario.standing = False
        else:
            mario.standing = True

        if keys[pg.K_UP] and not mario.jumping:
            mario.jump()

    pg.display.update()
pg.quit()
