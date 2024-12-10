import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    '''A class to represent a single star in the fleet'''

    def __init__(self, ai_game):
        '''initialize the star and set its position'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the star image
        self.image = pygame.image.load('media/mario_star.png')
        self.image = pygame.transform.scale(self.image, (80,80))
        self.rect = self.image.get_rect()

        # sart each new alien near the top left of the screen
        #self.rect.x = self.rect.width
        #self.rect.y = self.rect.height
        self.rect.x = 50
        self.rect.y = 50

        # stare the aliens exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        '''return True if alien is at the edge of screen'''
        screen_rect = self.screen.get_rect()
        return ( self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        '''move the alien to the right'''
        self.x += self.settings.star_speed * self.settings.stars_direction
        self.rect.x = self.x