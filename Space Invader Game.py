import math
import random 
import pygame
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800, 500))
background = pygame.image.load('background.png')
#mixer.music.load("background.wav")
#mixer.music.play(-1)
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
    
bulletImg = pygame.image.load('bullet.png')
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

def showscore(x,y):
    score = font.render("Score = "+ str(score_value),True,pygame.Color("red"))
    screen.blit(score,(x,y))
def gameovertext():
    overtext = over_font.render("Game Over",True,pygame.Color("green"))
    screen.blit(overtext,(200,250))
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def firebullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX)**2+(enemyY - bulletY)**2)
    return distance < 27
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                firebullet(bulletX,bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0
    playerX += playerX_change
    playerX = max(0,min(playerX,800-64))
    for i in range(6):
        if enemyY[i]>340:
            for j in range (6):
                enemyY[j] = 2000
            gameovertext()
            break
        enemyX[i]+= enemyX_change[i]
        if enemyX[i]<= 0 or enemyX[i]>=800-64:
            enemyX_change[i]*= -1
            enemyY[i] += enemyY_change[i]
        if collision(enemyX[i],enemyY[i],bulletX, bulletY):
            bulletY = 380
            bullet_state = "ready"
            score_value +=1
            enemyX[i] = random.randint(0,800-64)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)
    if bulletY <= 0:
        bulletY = 380
        bullet_state = "ready"
    elif bullet_state =="fire":
        firebullet(bulletX, bulletY)
        bulletY -= bulletY_change
    player(playerX, playerY)
    showscore(textX, textY)
    pygame.display.update()