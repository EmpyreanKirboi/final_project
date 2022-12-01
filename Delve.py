import sys
import pygame
import time
from delvesettings import Settings
from diver import Diver
from diver import depth

i = 0

pygame.init()


class Delve:
    def __init__(self):
        """Starts the game"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.image = pygame.image.load('images/startscreen.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Delve")

        self.diver = Diver(self)

    def run_game(self):
        """Start the main loop for the game."""
        global i
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
        global i
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.diver.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.diver.moving_left = True
        elif event.key == pygame.K_SPACE:
            i += 1
            self.diver.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.diver.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.diver.moving_left = False
        elif event.key == pygame.K_SPACE:
            self.diver.moving_up = False


            # Redraw the screen during each pass through the loop.


    def _update_screen(self):
        global depth
        """Update images on the screen, and flip to the new screen."""
        global i
        if i == 0:
            startscreen = Delve()
            startscreen.draw()
            pygame.display.flip()
            #print(i)
        if i > 0:
            self.settings.update()
            self.screen.fill(self.settings.bg_color)
            self.diver.gravity()
            self.image = pygame.image.load("images/diver_healthy.bmp")
            self.diver.update()
            self.diver.blitme()
            pygame.display.flip()
            #print(i)

        # Make the most recently drawn screen visible.

    def draw(self):
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    ai = Delve()
    ai.run_game()

