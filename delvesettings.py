from diver import depth
class Settings:
    """A class to store settings"""

    def __init__(self):
        # Screen Settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (32, 230, int(depth))
        #print(self.bg_color)

        # Diver Settings
        self.diver_speed = 5.0
        self.ship_limit = 3

    def update(self):
        self.bg_color = (32, 230, int(depth))
        
        print(self.bg_color)