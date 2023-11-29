# 12-1 Blue Sky
import sys
import pygame

from plane import Plane

class BlueSky:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")

        self.plane = Plane(self)

        self.bg_color = (135, 206, 235)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.plane.blitme()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()