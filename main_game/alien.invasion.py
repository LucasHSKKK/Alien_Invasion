import sys

import pygame

from settings import Settings
from space_ship import Space_Ship


class AlienInvasion:
    # manage game assets and resources
    def __init__(self):
        # initialize the game, and create game resources
        pygame.init()
        self.clock = pygame.time.Clock()
        self.Settings = Settings()
        self.screen = pygame.display.set_mode(
            (
                self.Settings.screen_width,
                self.Settings.screen_height,
            )
        )

        pygame.display.set_caption("Alien Invasion")

        self.ship = Space_Ship(self)

    def run_game(self):
        # starting the main loop
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen during each pass through the loop
            self.screen.fill(self.Settings.bg_color)
            self.ship.blitme()
            # make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
