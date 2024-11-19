# settings

class Settings:
    '''class to store settings'''

    def __init__(self):
        '''initilize game settings'''
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (140,36,200)

        # ship speed
        self.rocket_speed = 5

        #bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)