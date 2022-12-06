class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = delvesettings
        self.reset_stats()
        # Start alien invasion in an active state.
        self.game_active = True