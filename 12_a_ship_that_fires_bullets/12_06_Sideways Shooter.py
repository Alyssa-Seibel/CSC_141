import sys
import pygame
from settings_12_06 import Settings
from rocket_12_06 import Rocket
from bullet_12_06 import Bullet

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
        self.bullets = pygame.sprite.Group()

        self.bg_color = (140,36,200)

    def run_game(self):
        '''main loop'''
        while True:
            self._check_events()
            self.rocket.update()
            self.bullets.update()
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
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        '''respond to keypresses'''
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _fire_bullet(self):
        '''create a new bullet and add to the group'''
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
 
    def _update_screen(self):
        '''update images on the screen'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rocket.blitme()

        pygame.display.flip()

if __name__== '__main__':
    ai = AlienInvasion()
    ai.run_game()