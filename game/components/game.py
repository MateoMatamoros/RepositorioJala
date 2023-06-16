import time
import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.enemies.enemy_manager import EnemyManager

from game.utils.constants import BG, WALLPAPER,OVER, FONT_STYLE, ICON, ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import Spaceship

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.death_count = 0
        self.score = 0
        self.best_score = 0
        pygame.mixer.music.load('Music.mp3')
        pygame.mixer.music.play(3)

        self.menu = Menu ('Press Any Key to Start...', '', self.screen)

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()


    def run(self):
        # Game loop: events - update - draw
        self.score = 0
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.update_score()
        self.valide_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()  #implemenatr
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
            
        self.y_pos_bg += self.game_speed
    
    def show_menu(self):
        self.menu.reset_screen_color(self.screen)

        if self.death_count >0:
            self.menu.update_message(f'Score: {self.score} - Best Score {self.best_score}', f'Deaths: {self.death_count}')

        self.menu.draw(self.screen, self)
        self.menu.update(self)

    def update_score(self):
        self.score += 1
    
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (100, 100)
        self.screen.blit(text, text_rect)

    def valide_score(self):
        if self.score >= self.best_score:
            self.best_score = self.score