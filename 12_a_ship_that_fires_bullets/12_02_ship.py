import pygame

class Shooter:
    '''A class to manage ship'''

    def __init__(self, ai_game):
        '''Initialize the ship and set its starting position'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() # idk 
        

        # load the ship image and get its rect.
        self.image = pygame.image.load('media/space_ship.png')
        self.rect = self.image.get_rect()
    
        # start each new ship at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)