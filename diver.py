import pygame



class Diver:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the diver image and get its rect.
        self.image = pygame.image.load("images/diver_healthy.bmp")
        self.rect = self.image.get_rect()

        # start each diver at the upper center of the screen
        self.rect.x = 450
        self.rect.y = -100

        # Store a decimal value for the diver's horizontal position.
        self.x = float(self.rect.x)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

        # Update rect object from self.x.
    def update(self):
        """Update the ship's position based on the movement flag."""
        # update the ships x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_diver(self):
        """Center the diver on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)