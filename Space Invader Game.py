import math
import random 
import pygame
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800, 500))
backgroung = pygame.image.load('background.png')
mixer.music.load("background.wav")
mixer.music.play(-1)
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 380
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)
    
bulletImg = pygame.imave.load('bullet.png')
bulletX = 0
bulletY = 380
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)