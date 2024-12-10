import pygame 
from pygame.sprite import Sprite


class Shell(Sprite):
    ''' manage shell'''

    def __init__(self, ai_game):
        ''' create a shell object at the ships current position'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # create a shell rect at (0,0) and then set correct position.
        self.image = pygame.image.load('media/red_shell.png')
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect()

        # start the shell at mario's loction
        self.rect.midtop = ai_game.mario.rect.midtop

        #store the bullets position
        self.y = float(self.rect.y)

        

    def update(self):
        '''move the shell up the screen'''
        # update the exact position of the bullet
        self.y -= self.settings.shell_speed
        #update the rect position
        self.rect.y = self.y
        
    def draw_shell(self):
        '''draw the shell to the screen'''
        self.screen.blit(self.image, self.rect)
