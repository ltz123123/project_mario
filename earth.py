import pygame as pg


class wt_on_earth:  # block = (x,y,width,height)
    def __init__(self, block_tuple):
        self.x = block_tuple[0]
        self.y = block_tuple[1]
        self.width = block_tuple[2]
        self.height = block_tuple[3]

    def block(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

    def earth(self):
        return pg.Rect(self.x, self.y - 4, self.width, 4)

    def draw(self, mario, screen):
        if self.x - mario.x < 1200:
            pg.draw.rect(screen, (47, 79, 79), (50 + self.x - mario.x, self.y, self.width, self.height))


class Qmark(wt_on_earth):
    def __init__(self, block_tuple1):
        wt_on_earth.__init__(self, block_tuple1)
        self.broken = [False, False, False, False]

    def ceiling(self):
        return pg.Rect(self.x + 5, self.y + self.height + 4, self.width - 5, 4)

    def draw(self, mario, screen):
        if self.x - mario.x < 1200:
            if self.broken:
                pg.draw.rect(screen, (255, 255, 0), (50 + self.x - mario.x, self.y, self.width, self.height))
            else:
                pg.draw.rect(screen, (255, 255, 204), (50 + self.x - mario.x, self.y, self.width, self.height))

map_qmark = [Qmark((255, 215, 15, 15)),
             Qmark((335, 215, 15, 15)),
             Qmark((350, 150, 15, 15)),
             Qmark((365, 215, 15, 15))
             ]