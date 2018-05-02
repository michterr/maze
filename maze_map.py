import pygame
import unit
pygame.init()


class Level:
    def __init__(self, i):
        self.namber = i
        self.maze = Maze()
        self.level_screen = pygame.Surface(self.maze.maze_size)
        self.level_maze_group = pygame.sprite.Group()
        self.hero = unit.Hero(self.maze.hero_pozition)
        self.level_unit_group = pygame.sprite.Group()
        self.maze.add_level_groupe(self.level_maze_group)
        self.hero.add_level_groupe(self.level_unit_group)

    def render(self, win):
        self.level_maze_group.draw(self.level_screen)
        self.level_unit_group.draw(self.level_screen)
        win.blit(self.level_screen, (0, 0))
        self.movement()

    def movement(self):
        self.collide_wall()
        for un in self.level_unit_group:
            un.move_unit()

    def collide_wall(self):
        for wall in self.maze.wall:
            if pygame.sprite.collide_rect(self.hero, wall):
                if self.hero.movex > 0:
                    self.hero.rect.x -= 1
                elif self.hero.movex < 0:
                    self.hero.rect.x += 1
                elif self.hero.movey < 0:
                    self.hero.rect.y += 1
                elif self.hero.movey > 0:
                    self.hero.rect.y -= 1
                self.hero.movex = self.hero.movey = 0


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
