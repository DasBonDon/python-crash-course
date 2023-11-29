# 12-5 Keys
import sys
import pygame

class EmptyScreen:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Empty Screen")

        self.bg_color = (0, 0, 0)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print(f"Key pressed: {event.key}")
                elif event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    es = EmptyScreen()
    es.run_game()