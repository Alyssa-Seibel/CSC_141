import sys
import pygame
from settings import Settings
from mario import Mario
from bullet import Shell
from star import Star

class AlienInvasion:
    '''Game management'''

    def __init__(self):
        '''initialize the game, create resources'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.mario = Mario(self)
        self.shells = [] # store shell objects
        self.stars = pygame.sprite.Group()

        self._create_stars()

        # load layers
        self.layer1 = pygame.image.load('Blue Version/blue-back.png').convert_alpha() #furthest layer
        self.layer2 = pygame.image.load('Blue Version/blue-stars.png').convert_alpha() #mid
        #self.layer3 = pygame.image.load('Blue Version/asteroid-1.png').convert_alpha() # asteroid

        # scale layers
        self.layer1 = pygame.transform.scale(self.layer1, (self.settings.screen_width, self.settings.screen_height))
        self.layer2 = pygame.transform.scale(self.layer2, (self.settings.screen_width, self.settings.screen_height))
        #self.layer3 = pygame.transform.scale(self.layer3, (50,50))
    
        # background layer position
        self.layer1_x = 0
        self.layer2_x = 0
        #self.layer3_x = 0

        # background layer speed
        self.layer1_speed = .7 # slow
        self.layer2_speed = 1.7
        #self.layer3_speed = 1 # fast

        # generate random for asteroid
        #self.asteroid_x = random.randint(0, self.settings.screen_width - 200)
        #self.asteroid_y = random.randint(-200, -50)


    def run_game(self):
        '''main loop'''
        while True:
            self._check_events()
            self.mario.update()

            for shell in self.shells[:]:
                shell.update()

                if shell.rect.bottom <= 0:
                    self.shells.remove(shell)

                #self.asteroid_y += self.layer3_speed

                # reset asteroids position
                #if self.asteroid_y > self.settings.screen_height:
                    #self.asteroid_y = random.randint(-200,-50)
                    #self.asteroid_x = random.randint(0, self.settings.screen_width-50)
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
            self.mario.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.mario.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_shell()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        

    def _check_keyup_events(self,event):
        '''respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.mario.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.mario.moving_left = False

    def _create_stars(self):
        '''create a group of start'''
        # make a star
        star = Star(self)
        self.stars.add(star)
        star_width = star.rect.width

        current_x = star_width
        while current_x < (self.settings.screen_width - 2 * star_width):
            new_star = Star(self)
            new_star.x = current_x
            new_star.rect.x = current_x
            self.stars.add(new_star)
            current_x += 2 * star_width

    

    def _fire_shell(self):
        '''create a new bullet and add to the group'''
        new_shell = Shell(self)
        self.shells.append(new_shell)
        print(f"New shell fired at position: {new_shell.rect.midtop}")

    def _update_screen(self):
        '''update images on the screen'''
        self.layer1_x -= self.layer1_speed
        self.layer2_x -= self.layer2_speed
        #self.layer3_x-= self.layer3_speed

        if self.layer1_x <= -self.settings.screen_width:
            self.layer1_x = 0
        if self.layer2_x <= -self.settings.screen_width:
            self.layer2_x = 0
        #if self.layer3_x <= -self.settings.screen_width:
            #self.layer3_x = 0

        self.screen.blit(self.layer1, (self.layer1_x, 0))
        self.screen.blit(self.layer1, (self.layer1_x + self.settings.screen_width, 0))
        self.screen.blit(self.layer2, (self.layer2_x, 0))
        self.screen.blit(self.layer2, (self.layer2_x + self.settings.screen_width, 0))
        #self.screen.blit(self.layer3,(self.layer3_x, 0))
        #self.screen.blit(self.layer3, (self.layer2_x + self.settings.screen_width, 0))

        #self.screen.blit(self.layer3, (self.asteroid_x, self.asteroid_y))

        for shell in self.shells:
            shell.draw_shell()
        self.mario.blitme()
        self.stars.draw(self.screen)

        pygame.display.flip()

if __name__== '__main__':
    ai = AlienInvasion()
    ai.run_game()