import sys

import pygame


class AlienInvasion:
    # manage game assets and resources
    def __init__(self):
        # initialize the game, and create game resources
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")
        # set the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        # starting the main loop
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)
            # make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
