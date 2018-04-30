import pygame
pygame.init()


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = (24, 24)
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()

    def set_location(self, x, y):
        self.rect.x = x * self.size[0]
        self.rect.y = y * self.size[1]

    def dye(self, color):
        if color == 1:
            self.image.fill((0, 138, 23))
        elif color == 2:
            self.image.fill((255, 172, 37))


class Unit(Tile):
    def __init__(self):
        Tile.__init__(self)
        self.movex = 0
        self.movey = 0

    def add_level_groupe(self, level):
        level.add(self)

    def move_right(self):
        if self.movex == 0:
            self.movex = self.size[0]

    def move_left(self):
        if self.movex == 0:
            self.movex = -self.size[0]

    def move_up(self):
        if self.movey == 0:
            self.movey = -self.size[1]

    def move_down(self):
        if self.movey == 0:
            self.movey = self.size[1]

    def move_unit(self):
        if self.movex > 0:
            self.rect.x += 1
            self.movex -= 1
        elif self.movex < 0:
            self.rect.x -= 1
            self.movex += 1
        elif self.movey < 0:
            self.rect.y -= 1
            self.movey += 1
        elif self.movey > 0:
            self.rect.y += 1
            self.movey -= 1


class Hero(Unit):
    def __init__(self, start_location):
        Unit.__init__(self)
        self.set_location(start_location[0], start_location[1])
        self.image.fill((255, 255, 255))




