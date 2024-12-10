# settings

class Settings:
    '''class to store settings'''

    def __init__(self):
        '''initilize the game's static settings'''
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)

        # ship settings
        self.mario_speed = 5
        self.mario_limit = 3
        #bullet settings
        self.shell_speed = 10
        self.shell_width = 10
        self.shell_height = 20
        # alien settings
        self.star_speed = 2.5
        self.stars_drop_speed = 10

        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # how quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        '''initialize settings that change througout the game'''
        self.mario_speed = 5
        self.shell_speed = 5
        self.star_speed = 3

        # fleet_direcrion of 1 represents right and -1 left
        self.stars_direction = 1

        # scoring settings
        self.star_points = 50

    
    def increase_speed(self):
        '''Increase speed settings and alien point values'''
        self.mario_speed *= self.speedup_scale
        self.shell_speed *= self.speedup_scale
        self.star_speed *= self.speedup_scale

        self.star_points = int(self.star_points * self.score_scale)
        print(self.star_points)
        