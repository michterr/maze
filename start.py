import  pygame, maze_map
from pygame.locals import *

pygame.init()

class Game:
    def __init__(self):
        self.size = (360, 360)
        self.run = True
        self.win = self.open_window()
        self.world = maze_map.World(self.win)

    def open_window(self):
        return pygame.display.set_mode(self.size)

    def actions(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.run = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    pass
                elif e.key == pygame.K_RIGHT:
                    pass
                elif e.key == pygame.K_UP:
                    pass
                elif e.key == pygame.K_DOWN:
                    pass
            if e.type == pygame.KEYUP:
                pass

    def main_loop(self):
        while self.run:
            self.actions()
            self.world.render_all((0, 0))
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.main_loop()