import sys
import pygame
import time

from delvesettings import Settings

pygame.init()
class Delve:
    def __init__(self):
        """Starts the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.image = pygame.image.load('images/startscreen.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Delve")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

        # Make the most recently drawn screen visible.

if __name__ == '__main__':
    dv = Delve()
    dv.run_game()

