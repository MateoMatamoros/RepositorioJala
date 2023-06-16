import pygame
from game.utils.constants import ENEMY_1, ENEMY_2, FONT_STYLE, ICON, OVER, SCREEN_HEIGHT, SCREEN_WIDTH, WALLPAPER



class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT //2

    def __init__(self, message, message_2, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 50)
        self.text = self.font.render(message, True, (255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)
        self.text_2 = self.font.render(message_2, True, (255,255,255))
        self.text_rect_2 = self.text_2.get_rect()
        self.text_rect_2.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 200)
        self.wallpaper = pygame.transform.scale (WALLPAPER, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.icon = pygame.transform.scale (ICON, (80,120))
        self. game_over = pygame.transform.scale (OVER, (350,50))
        self.enemy_1 = pygame.transform.scale(ENEMY_1,(80,120))
        self.enemy_2 = pygame.transform.scale(ENEMY_2,(80,120))

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw (self, screen, game):
        screen.blit(self.wallpaper, (0, 0))
        screen.blit(self.icon, (self.HALF_SCREEN_WIDTH - 50, self.HALF_SCREEN_HEIGHT -50))
        screen.blit(self.enemy_1, (self.HALF_SCREEN_WIDTH + 100, self.HALF_SCREEN_HEIGHT -270))
        screen.blit(self.enemy_2, (self.HALF_SCREEN_WIDTH - 200, self.HALF_SCREEN_HEIGHT -270))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text_2, self.text_rect_2)
        if game.death_count >0:
            screen.blit(self.game_over, (self.HALF_SCREEN_WIDTH - 190, self.HALF_SCREEN_HEIGHT -120))

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def update_message(self, message, message_2):
        self.text = self.font.render(message, True, (255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)
        self.text_2 = self.font.render(message_2, True, (255,255,255))
        self.text_rect_2 = self.text_2.get_rect()
        self.text_rect_2.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 200)
