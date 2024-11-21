# settings

class Settings:
    '''class to store settings'''

    def __init__(self):
        '''initilize game settings'''
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)

        # ship speed
        self.mario_speed = 5
                #bullet settings
        self.shell_speed = 8
        self.shell_width = 10
        self.shell_height = 20
        