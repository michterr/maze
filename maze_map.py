import pygame
pygame.init()

class Level:
    def __init__(self, screen_size):
        self.maze = Maze()
        self.level_screen = pygame.Surface(screen_size)
        self.level_screen.fill((40, 40, 40))
        self.hero = Hero()
        self.actions = False

    def move_maze(self):

        x = self.maze.poz[0]
        y = self.maze.poz[1]
        if self.hero.movex < 0:
            #self.hero.colide(self.maze.wall)
            x = self.maze.poz[0] - 1
            self.hero.movex += 1
            self.actions = True
        else:
            self.actions = False
        self.maze.poz = (x, y)

    def render(self, win):
        self.move_maze()
        win.blit(self.level_screen, (0, 0))
        win.blit(self.maze.maze_image, self.maze.poz)
        win.blit(self.hero.image, (self.hero.rect.x, self.hero.rect.y))


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


class Hero(Unit):
    def __init__(self):
        Unit.__init__(self)
        self.set_location(7, 7)
        self.image.fill((240, 240, 50))

    def move_right(self):
        self.movex = - self.size[0]

    def colide(self, wall):
        for w in wall:
            if pygame.sprite.collide_rect(self, w):
                self.movex = 0

class Maze:
    def __init__(self):
        self.maze_tile = pygame.sprite.Group()
        self.wall = []
        self.maze_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.maze_image = pygame.Surface((len(self.maze_map[0]) * 24, len(self.maze_map) * 24))
        self.hero_pozition = (1, 1)
        self.poz = (6 * 24, 6 * 24)
        self.render()

    def render(self):
        y = 0
        for xline in self.maze_map:
            x = 0
            for loc in xline:
                tile_floor = Tile()
                tile_floor.dye(loc)
                tile_floor.set_location(x, y)
                self.maze_tile.add(tile_floor)
                if loc == 1:
                    self.wall.append(tile_floor)
                x += 1
            y += 1
        self.maze_tile.draw(self.maze_image)


