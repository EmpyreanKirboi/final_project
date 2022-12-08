from diver import depth
class Settings:
    """A class to store settings"""

    def __init__(self):
        # Screen Settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (32, 230, 200)
        #print(self.bg_color)

        # Diver Settings
        self.diver_speed = 1.0

        # Enemy Settings
        self.enemy_speed = 0.5

        self.diver_limit = 1