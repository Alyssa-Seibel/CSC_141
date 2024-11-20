# rocket

import pygame

class Mario:
    '''manage Mario'''

    def __init__(self, ai_game):
        '''initialize the ship and set starting point'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship and get its rect
        original_image = pygame.image.load('media/mario_kart.png')
        self.image = pygame.transform.scale(original_image, (100,100))
        self.rect = self.image.get_rect()

        # start each new ship at the bottome
        self.rect.midbottom = self.screen_rect.midbottom

        # store a float for the ships exact horizontal position
        self.x = float(self.rect.x)


        # movement flags
        self.moving_right = False
        self.moving_left = False

        # direction of the rocket
        self.facing_right = True

    def update(self):
        '''update mario's position'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.mario_speed
            if self.facing_right:
                self.image = pygame.transform.flip(self.image, True, False)
                self.facing_right = False # facing right
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.mario_speed
            if not self.facing_right:
                self.image = pygame.transform.flip(self.image, True,False)
                self.facing_right = True # facing left
           
        # update rect
        self.rect.x = self.x

    def blitme(self):
        '''draw mario at current location'''
        self.screen.blit(self.image, self.rect)