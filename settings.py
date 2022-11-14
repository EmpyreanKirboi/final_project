class Settings:
    """A class to store all settings for Sideways Shooter."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 230, 230)

        # Ship settings
        self.ship_speed = 1.0
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 6.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (0, 60, 60)
        self.bullets_allowed = 3

        # Alien settings.
        #  alien_frequency controls how often a new alien appear.s
        #    Higher values -> more frequent aliens. Max = 1.0.
        self.alien_frequency = 0.015
        self.alien_speed = 0.3