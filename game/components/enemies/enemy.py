import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import DEFAULT_TYPE, ENEMY_1, ENEMY_2, HEART_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE

class Enemy(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    Y_POS = 20
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    SPEED_Y = 1
    SPEED_X = [5, 6, 7, 8, 9, 10]
    MOV_X = {0: 'left', 1: 'right'}
    IMAGE = {1: ENEMY_1, 2: ENEMY_2}


    def __init__(self):
        self.image = self.IMAGE[random.randint(1,2)]
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS_LIST[random.randint(0, 10)]
        self.speed_x = self.SPEED_X[random.randint(0, 5)]
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0
        self.type = 'enemy'
        self.shooting_time = pygame.time.get_ticks()+500

    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game)

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        
        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

        if self.rect.colliderect(game.player.rect):
                if game.player.power_up_type == HEART_TYPE:
                    if self.rect.colliderect(game.player.rect): 
                        game.enemy_manager.enemies.remove(self)   
                        game.player_has_power_up = False
                        game.player.power_up_type = DEFAULT_TYPE

                elif game.player.power_up_type != SHIELD_TYPE and game.player.power_up_type != HEART_TYPE: 
                    game.death_count += 1
                    game.playing = False
                    pygame.time.delay(1100)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <=10):
            self.movement_x = 'right'
            self.index = 0
    
    def shoot(self, game):
        current_time = pygame.time.get_ticks()
        round_time = round((self.shooting_time - current_time)/1000)
        if round_time <= 0:
            bullet = Bullet(self)
            game.bullet_manager.add_bullet(bullet, game)
            self.shooting_time = current_time + 2000