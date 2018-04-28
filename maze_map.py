import pygame, unit
pygame.init()


class Level():
    def __init__(self, i):
        self.namber = i
        self.maze = Maze()
        self.hero = unit.Hero(self.maze.hero_pozition)
        self.level_screen = pygame.Surface(self.maze.maze_size)
        self.level_maze_group = pygame.sprite.Group()
        self.level_unit_group = pygame.sprite.Group()
        self.actions = False


    def render(self, win):
        self.hero.add_level_groupe(self.level_unit_group)
        self.maze.add_level_groupe(self.level_maze_group)
        self.level_maze_group.draw(self.level_screen)
        self.level_unit_group.draw(self.level_screen)
        win.blit(self.level_screen, (0, 0))


class Maze:
    def __init__(self):
        self.maze_tile = pygame.sprite.Group()
        self.wall = []
        self.maze_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.hero_pozition = (1, 1)
        self.maze_size = (len(self.maze_map[0]) * 24, len(self.maze_map[0]) * 24)

    def add_level_groupe(self, level):
        y = 0
        for xline in self.maze_map:
            x = 0
            for loc in xline:
                tile_floor = unit.Tile()
                tile_floor.dye(loc)
                tile_floor.set_location(x, y)
                level.add(tile_floor)
                if loc == 1:
                    self.wall.append(tile_floor)
                x += 1
            y += 1
