import pygame, maze_map
from pygame.locals import *

pygame.init()

class Game:
    def __init__(self):
        self.size = (360, 360)
        self.run = True
        self.win = self.open_window()
        self.levels = []
        self.create_level()

    def open_window(self):
        return pygame.display.set_mode(self.size)

    def create_level(self):
        self.levels.append(maze_map.Level(0))

    def actions(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.run = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    self.levels[0].hero.move_left()
                elif e.key == pygame.K_RIGHT:
                    self.levels[0].hero.move_right()
                elif e.key == pygame.K_UP:
                    self.levels[0].hero.move_up()
                elif e.key == pygame.K_DOWN:
                    self.levels[0].hero.move_down()
            if e.type == pygame.KEYUP:
                pass

    def main_loop(self):
        while self.run:
            self.actions()
            self.levels[0].render(self.win)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.main_loop()