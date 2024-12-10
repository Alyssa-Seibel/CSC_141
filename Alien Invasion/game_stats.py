

class GameStats:
    '''Track statistics for Alien Invasion'''

    def __init__(self, ai_game):
        '''initialize statistics.'''
        self.settings = ai_game.settings
        self.reset_stats()

        # high score should never be reset
        self.high_score = 0
    
    def reset_stats(self):
        '''initialize stats that can change during the game'''
        self.marios_left = self.settings.mario_limit
        self.score = 0
        self.level = 1