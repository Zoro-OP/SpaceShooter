import pygame
import random
import math

from sqlalchemy import true


#Initialize the pygame 
pygame.init()


#Create the screen

screen = pygame.display.set_mode((800, 600))


#background 

background = pygame.image.load('background.png')



#Title and Icon

pygame.display.set_caption("Space Shooter")

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


#player

playerImg= pygame.image.load('aircraft.png')

playerX=370

playerY=480

playerX_change= 0



#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range (num_of_enemies):

    enemyImg.append(pygame.image.load('alien.png'))

    enemyX.append(random.randint(0, 735))

    enemyY.append(random.randint(50, 150))

    enemyX_change.append(1)

    enemyY_change.append(40)



#bullet 


#ready- can't see the bullet

#fire- bullet moving


bulletImg= pygame.image.load('bullet.png')

bulletX= 0

bulletY= 480

bulletX_change= 0

bullet_state = "ready"

score = 0

def player(x, y):

    screen.blit(playerImg, (x, y))



def enemy(x, y, i):

    screen.blit(enemyImg[i], (x, y))



def fire_bullet(x, y):
    global bullet_state

    bullet_state = "fire"

    screen.blit(bulletImg, (x + 16, y+ 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance= math.sqrt(math.pow (enemyX - enemyY, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


#Game loop 

running = True

while running:

    #RGB= Red, Green, Blue

    screen.fill((0, 150, 120))

    #background Image

    screen.blit(background, (0, 0))


    # playerX += 0.1


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
    


        #if keystroke is pressed check wheather its right or left

        if event.type == pygame.KEYDOWN:

            # print("A keystroke is pressed")

            if event.key == pygame.K_LEFT: #For key left arrow

                playerX_change= -2

            if event.key == pygame.K_RIGHT: #For key right arrow

                playerX_change= 2

            if event.key == pygame.K_a:     #For key a

                playerX_change= -2

            if event.key == pygame.K_d:     #for key d

                playerX_change= 2

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    #multiple bullet same time
                    bulletX = playerX
                    fire_bullet(playerX, bulletY )


        if event.type == pygame.KEYUP:

            if event.key == pygame. K_LEFT or event.key == pygame.K_RIGHT:

                playerX_change= 0

            elif event.key == pygame. K_a or event.key == pygame.K_d:

                playerX_change= 0

                # print("Keystroke has been released")



    # 5 = 5 + - 0.1 -> 5 = - 0.1

    # 5 = 5 + 0.1



    #Checking for boundaries of aircraft, so that it'll stay inside the screen 


    playerX += playerX_change


    if playerX <= 0:

        playerX = 0


    elif playerX >= 736:

        playerX = 736




    #Enemy Movement

    for i in range(num_of_enemies):

        enemyX[i] += enemyX_change[i]


    if enemyX[i] <= 0:

        enemyX_change[i] = 1

        enemyY[i] += enemyY_change[i]


    elif enemyX[i] >= 736:

        enemyX_change[i] = -1

        enemyY[i] += enemyY_change[i]

    #collision
    collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)

        enemyX[i]=random.randint(0, 735)
        enemyY[i]=random.randint(50, 150)

    enemy(enemyX[i], enemyY[i], i)


    #bullet movement
    if bulletY <=0 :
        bulletY = 480
        bullet_state = "ready"


    if bullet_state is "fire":

        fire_bullet(bulletX, bulletY)

        bulletY -= 5

   



    player(playerX, playerY)

    pygame.display.update()




