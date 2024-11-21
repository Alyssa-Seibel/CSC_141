import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    '''A class to represent a single star in the fleet'''

    def __init__(self, ai_game):
        '''initialize the star and set its position'''
        super().__init__()
        self.screen = ai_game.screen

        # load the star image
        self.image = pygame.image.load('media/mario_star.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (80,80))

        # sart each new alien near the top left of the screen
        #self.rect.x = self.rect.width
        #self.rect.y = self.rect.height
        self.rect.x = 50
        self.rect.y = 50


        # stare the aliens exact horizontal position
        self.x = float(self.rect.x)
