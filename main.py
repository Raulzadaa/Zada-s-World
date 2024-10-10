import pygame, sys
from settings import *
from floor import Floor


class Game:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("""Zada's World""")

        self.floor = Floor()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill("black")
            self.floor.run()
            pygame.display.update()
            self.clock.tick(fps)

if __name__ == '__main__':
    game = Game()
    game.run()