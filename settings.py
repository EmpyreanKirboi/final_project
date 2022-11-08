class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_image = (40, 20, 40)


        # Ship Settings
        self.ship_speed = 0.8

        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 0, 0)
        self.bullets_allowed = 20