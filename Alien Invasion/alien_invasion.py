import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

        # create an instance to store game stats
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.mario = Mario(self)
        self.shells = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_stars()

        # start alien invasion in an inactive state
        self.game_active = False

        # Make the Play button.
        self.play_button = Button(self, "Play")




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

        # audio
        music = pygame.mixer.Sound('media/music.mp3')
        music.set_volume(.2)
        music.play(loops = -1)

    def run_game(self):
        '''main loop'''
        while True:
            self._check_events()

            if self.game_active:
                self.mario.update()
                self._update_shells()
                self._update_stars()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        '''start a new game when the player clicks Play'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # reset the game settings
            self.settings.initialize_dynamic_settings()

            # reset the game statistics
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_marios()
            self.game_active = True

            # get rid of any remaining bullets and aliens
            self.shells.empty()
            self.stars.empty()

            # create a new fleet and center the ship
            self._create_stars()
            self.mario.center_mario()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)
                    
                
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
        #self.stars.add(star)
        star_width, star_height  = star.rect.size

        # adjust spacing here
        x_spacing = 1.2 #hor
        y_spacing = 1.2 #vert

        current_y = star_height
        while current_y < (self.settings.screen_height - 3 * star_height):
            current_x = star_width # reset x for each new row
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += x_spacing * star_width
            current_y += y_spacing * star_height

            

    def _create_star(self, x_position, y_position):
        '''create an alien and place it in the row'''
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)



    def _check_stars_edges(self):
        '''respond appropriately if any aliens have reached an edge'''
        for star in self.stars.sprites():
            if star.check_edges():
                self._change_stars_direction()
                break



    def _change_stars_direction(self):
        '''drop the entire fleet and change the fleet's direction'''
        for star in self.stars.sprites():
            star.rect.y += self.settings.stars_drop_speed
        self.settings.stars_direction *= -1



    def _fire_shell(self):
        '''create a new bullet and add to the group'''
        new_shell = Shell(self)
        self.shells.add(new_shell)
        



    def _update_shells(self):
        '''update position of bullets and get rid of old shells'''
        # update shell positon
        self.shells.update()
        # check for any bullets that have hit aliens
        #  if so, get rid of the bullet and aliens
    

        # get rid of bullets that disappeared
        for shell in self.shells.copy():
            if shell.rect.bottom <= 0:
                self.shells.remove(shell)

        self._check_shell_star_collision()



    def _check_shell_star_collision(self):
        '''respond to bullet-alien collision'''
        # remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(
            self.shells, self.stars, True, True)
        
        if collisions:
            for stars in collisions.values():
                self.stats.score += self.settings.star_points * len(stars)
            #self.stats.score += self.settings.star_points
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.stars:
            # destroy exisiting bullets and create new fleet
            self.shells.empty()
            self._create_stars()
            self.settings.increase_speed()

            # increase level.
            self.stats.level += 1
            self.sb.prep_level()



    def _mario_hit(self):
        '''respond to the ship being hit by an alien'''
        if self.stats.marios_left> 0:
            # decrement ships_lelft, and update scoreboard
            self.stats.marios_left -= 1
            self.sb.prep_marios()

            # get rid of any remaining bullets and aliens
            self.shells.empty()
            self.stars.empty()

            # create a new fleet and cneter the ship
            self._create_stars()
            self.mario.center_mario()

            # pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_stars(self):
        '''update the positions of all aliens in the fleet'''
        self._check_stars_edges()
        self.stars.update()

        # look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.mario, self.stars):
            self._mario_hit()

        # look for aliens hitting th ebottom of the screen
        self._check_stars_bottom()

    def _check_stars_bottom(self):
        '''check if any aliens have reached the bottom of the screen'''
        for star in self.stars.sprites():
            if star.rect.bottom >= self.settings.screen_height:
                # treat this the same as if the ship got hit
                self._mario_hit()
                break

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

        # draw the score info
        self.sb.show_score()

        # Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__== '__main__':
    ai = AlienInvasion()
    ai.run_game()