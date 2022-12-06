import pygame
import time

a = 0
depth = 0
class Diver:
    """A class to manage the ship."""




    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        a = ai_game.screen.get_rect()
        #print(a)

        # Load the diver image and get its rect.

        from timing import skin
        self.image = skin
        self.rect = self.image.get_rect()


        # start each diver at the upper center of the screen

        self.rect.midtop = self.screen_rect.midtop
        self.rect.y -= 200
        self.movey = 0

        # Store a decimal value for the diver's horizontal position.
        self.x = float(self.rect.x)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

        # Update rect object from self.x.
    def update(self):
        global depth
        """Update the ship's position based on the movement flag."""
        # update the ships x value, not the rect.
        self.rect.y = self.rect.y + self.movey

        if self.moving_right and self.rect.right < self.screen_rect.right + 470:
            self.x += self.settings.diver_speed
        if self.moving_left and self.rect.left > -500:
            self.x -= self.settings.diver_speed
        if self.moving_up:
            self.movey = 0
            self.movey -= 1.50
        if self.rect.bottom > self.screen_rect.bottom + 480:
            depth += 1
            #print(depth)
            self.rect.y = -300

        # Update rect object from self.x.
        self.rect.x = self.x

    def gravity(self):
        self.movey += 0.04



    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_diver(self):
        """Center the diver on the screen."""
        self.x = float(self.rect.x)