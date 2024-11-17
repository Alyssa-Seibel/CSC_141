# rocket

import pygame

class Rocket:
    '''manage ship'''

    def __init__(self, ai_game):
        '''initialize the ship and set starting point'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship and get its rect
        self.image = pygame.image.load('media/space_ship.png')
        self.rect = self.image.get_rect()

        # start each new ship at the bottome
        self.rect.bottom = self.screen_rect.bottom
        self.rect.left = self.screen_rect.left

        # store a float for the ships exact horizontal position
        self.x = float(self.rect.x)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''update the ships position'''
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
        # update rect
        self.rect.x = self.x

    def blitme(self):
        '''draw ship at current location'''
        self.screen.blit(self.image, self.rect)