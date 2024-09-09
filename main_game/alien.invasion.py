import sys

import pygame


class AlienInvasion:
    # manage game assets and resources
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set.mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        # starting the main loop
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        # make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
