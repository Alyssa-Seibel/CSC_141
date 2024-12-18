import sys
import pygame
from rocket_settings_12_04 import Settings
from rocket_12_04 import Rocket

class AlienInvasion:
    '''Game management'''

    def __init__(self):
        '''initialize the game, create resources'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.rocket = Rocket(self)

        self.bg_color = (140,36,200)

    def run_game(self):
        '''main loop'''
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)

    
    def _check_events(self):
        '''respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    
                
    def _check_keydown_events(self,event):
        '''respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        '''respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False

    def _update_screen(self):
        '''update images on the screen'''
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        pygame.display.flip()

if __name__== '__main__':
    ai = AlienInvasion()
    ai.run_game()