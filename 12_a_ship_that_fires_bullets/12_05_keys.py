import sys
import pygame
from setting_12_05 import Settings


class KeyGame:
    '''Manage game'''

    def __init__(self):
        '''initialize the game'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Key Game")


    def run_game(self):
        '''start the main loop for the game'''
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        '''respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        '''respond to keypress'''

        print(f"Key pressed: {pygame.key.name(event.key)}")
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()

if __name__ == '__main__':

    kg = KeyGame()
    kg.run_game()