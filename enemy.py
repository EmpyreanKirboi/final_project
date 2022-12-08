import pygame
import time
import random
from pygame.sprite import Sprite

a = 0
depth = 0
class Enemy(Sprite):
    """A class to manage the enemy."""




    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        a = ai_game.screen.get_rect()
        #print(a)

        # Load the diver image and get its rect.

        from timing import skin
        self.image = pygame.image.load("images/angler.bmp")
        self.rect = self.image.get_rect()

        #self.enemy_rect = self.rect.x, self_rect.y

        # start each diver at the upper center of the screen

        self.rect.y = random.randint(50, 200)
        self.rect.x = random.randint(50, 200)

        # Store a decimal value for the diver's horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        from diver import depth, pos_x, pos_y
        """Update the ship's position based on the movement flag."""
        # update the ships x value, not the rect.
        #if depth == 1:
            #self.rect.y = random.randint(50, 200)
            #self.rect.x = random.randint(50, 200)
        self.rect.y = pos_y
        self.rect.x = pos_x
        if depth > 5:
            self.image = pygame.image.load("images/killcrab.png")
        if depth > 9:
            self.image = pygame.image.load("images/idol.bmp")
            self.rect.y = 2000
            self.rect.x = 2000




    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)