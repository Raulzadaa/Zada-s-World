import pygame, sys
from settings import *
from floor import Floor , grass_field


class Game:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("""Zada's World""")
        self.icon_image = pygame.image.load("""C:/Users/Adm/Desktop/Zada's World/graphics/fly_castle.jpg""")
        pygame.display.set_icon(self.icon_image)
        
        self.floor = Floor()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill("black")
            self.screen.blit(grass_field, (0, 0))
            self.floor.run()
            pygame.display.update()
            self.clock.tick(fps)

if __name__ == '__main__':
    game = Game()
    game.run()