import sys
import pygame
from Settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class Alien_invasion:
    def __init__(self) -> None:
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((1366,768))
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height
        icon = pygame.image.load("games\\images\\logo.ico")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("alein invasion")
        self.game_active = False
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.score_board = Scoreboard(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self,"Play")

        self.clock = pygame.time.Clock()
        

        

    def rungame(self):
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()                       
                self._update_bullet()
                self._update_aliens()


            self._update_events()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_event(event)
                          
                
                elif event.type == pygame.KEYUP:
                     self._check_keyup_event(event)


    def _check_keydown_event(self , event):
         if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
         elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
         elif event.key == pygame.K_ESCAPE:
             sys.exit()
         elif event.key == pygame.K_SPACE:
             self._fire_bullet()
    
    def _check_keyup_event(self , event):
         if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
         elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
         
    
    def _update_events(self):
        self.screen.fill(self.setting.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme() 
        self.aliens.draw(self.screen) 
        self.score_board.show_score()
        if not self.game_active:
            self.play_button.draw_button()          
        pygame.display.flip()
         
    def _fire_bullet(self):
        if len(self.bullets) < self.setting.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)   

    def _update_bullet(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0 :
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collision()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
    
    def _check_bullet_alien_collision(self):
        collisions  = pygame.sprite.groupcollide(self.bullets , self.aliens , True , True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.setting.alien_points * len(aliens)
            self.score_board.prep_score()
            self.score_board.check_high_score()

        if not self.aliens:
            self.aliens.empty()
            self.bullets.empty()
            self.setting.increase_speed()
            self.stats.level += 1
            self.score_board.prep_level()

    
    def _create_fleet(self):
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size

        current_x , current_y = alien_width , alien_height
        while current_y < (self.setting.screen_height - 3 * alien_height):
            while current_x < (self.setting.screen_width - 2 * alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self,x_position,y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany( self.ship , self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()


    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1

    def _ship_hit(self):
        
        if self.stats.ship_left >0:
            self.stats.ship_left -= 1
            self.score_board.prep_ships()

            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)

        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.setting.screen_height:
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.stats.reset_stats()
            self.score_board.prep_score()
            self.score_board.prep_level()
            self.score_board.prep_ships()
            self.game_active = True
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
            self.setting.initialize_dynamic_settings()




            

    
ai: Alien_invasion = Alien_invasion()
ai.rungame()

           