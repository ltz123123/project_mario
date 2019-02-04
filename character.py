import pygame as pg


class character(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.width = 10
        self.height = 20
        self.vel = 5
        self.jumping = False

    def hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

    def accelerate():
        ''

    def jump(self):
        self.dy = -22

    def draw(self, screen):
        pg.draw.rect(screen, (255, 255, 255), pg.Rect(50, self.y, self.width, self.height))
