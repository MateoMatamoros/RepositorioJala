import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/Heart.png'))

OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, 'Other/Explosion.png'))

WALLPAPER = pygame.image.load(os.path.join(IMG_DIR, 'Other/Wallpaper.png'))

WALLPAPER2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Wallpaper2.png'))

BULLETS = pygame.image.load(os.path.join(IMG_DIR, 'Other/Bullets.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
HEART_TYPE = 'heart'
BULLETS_TYPE = 'burst'
MINIATURE_TYPE = 'miniature'
BOMB_TYPE = 'bomb'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'
FONT_STYLE1 = 'ethnocentric rg.otf'
