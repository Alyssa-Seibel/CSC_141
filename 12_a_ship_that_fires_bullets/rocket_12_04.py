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
        self.rect.midbottom = self.screen_rect.midbottom

        # store a float for the ships exact horizontal position
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''update the ships position'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

        # update rect
        self.rect.x = self.x

    def blitme(self):
        '''draw ship at current location'''
        self.screen.blit(self.image, self.rect)