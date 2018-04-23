import pygame

pygame.init()


class World:
    pass


class Tile(World):
    def __init__(self):
        self.size = (32, 32)
        self.surf = pygame.Surface(self.size)
        self.x = self.y = 0

    def render(self, screen_dest):
        screen_dest.blit(self.surf, (self.x * self.size[0], self.y * self.size[1]))

    def dye(self, color):
        self.surf.fill(color)


class Hero(Tile):
    def __init__(self):
        Tile.__init__(self)
        self.x = self.y = 1

    def move_righr(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1


class Maze:
    def __init__(self):
        self.create_maze()

    def create_maze(self):

        self.maze_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.maze = pygame.Surface((len(self.maze_map[0]) * 32, len(self.maze_map) * 32))

    def render(self, win):
        tileFloor = Tile()
        cl = 0
        y = 0
        for xline in self.maze_map:
            x = 0
            for loc in xline:
                if loc == 1:
                    color = (0, 138, 23)
                elif loc == 2:
                    color = (255, 172, 37)
                tileFloor.dye(color)
                tileFloor.x = x
                tileFloor.y = y
                tileFloor.render(self.maze)
                x += 1
            y += 1
        win.blit(self.maze, (0, 0))
