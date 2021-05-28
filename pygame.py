# CapeStone Project 2 Task 15: 
# Objective of the game - dodge the 4 enemies to get to the party prize during lockdown
# Player can move diagonally, left, right, up, down during play

# Import packages
import sys, pygame
import random  

# Initialize the pygame modules
pygame.init()

# The screen width and a height.
screen_width = 1300
screen_height = 650
screen = pygame.display.set_mode((screen_width,screen_height))

# This creates the players using the images in the same folder 
#player = pygame.image.load("player.png")
player = pygame.image.load("player.png")
enemy = pygame.image.load("image.png")
enemy1 = pygame.image.load("yellow_ghost.png")
enemy2 = pygame.image.load("coronavirus.png")
enemy3 = pygame.image.load("pink_ghost.png")
prize = pygame.image.load("prize.png")

# Boundary detection for width and height of the images
image_height = player.get_height()
image_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_height()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_height()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_height()

prize_height = prize.get_height()
prize_width = prize.get_height()

print("The Goal of the game is to dodge the 4 enemies to get to the Party prize during Lockdown")

# Store the positions of the player as variables
playerXPosition = 400
playerYPosition = 200

# Makes Enemy start off screen at a random y position
enemyXPosition =  screen_height
enemyYPosition = (0)

# Makes Enemy1 start at random mid screen
enemy1XPosition =  screen_height
enemy1YPosition =  screen_height

# Makes Enemy2 start at random mid screen
enemy2XPosition =  screen_width
enemy2YPosition = (0)

#  Makes Enemy3 start at random mid screen
enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(3, screen_height - enemy3_height)

# Makes the prize start at a random position
prizeXPosition = screen_width
prizeYPosition = 500

# Boolean values set at False to test conditions
keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# Game Loop
while 1:
    
# Clears the screen.
    screen.fill(0) 
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

# Updates the screen   
    pygame.display.flip() 

# Loops through events in the game.
    for event in pygame.event.get():
    
# Event checks if the user quits to exit the program 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

# Event to check if the user presses a key down
        if event.type == pygame.KEYDOWN:
        
# Test if the key pressed is the one we want        
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

# Event checks if the key is up(i.e. not pressed)
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
# Makes sure that the user does not move the player above the window(0,0)   
    if keyUp == True:
        if playerYPosition > 0 : 
            playerYPosition -= 1
# Makes sure that the user does not move the player below the window           
    if keyDown == True:
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1
# Addition for Left to right and diagonal movement of the player
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1
  
# Bounding box for the player:
    playerBox = pygame.Rect(player.get_rect())
    
# PlayerBox positioned to the player's position
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
# Bounding box for Enemy:
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

# Bounding box for Enemy1
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

# Bounding box for Enemy2
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

# Bounding box for Enemy3
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

# Bounding box for the Prize
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

# Test collision of the boxes:
    if playerBox.colliderect(enemyBox) or playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
    
# Display losing status to the user: 
        print("You lose!")

# Quit game and exit window: 
        pygame.quit()
        exit(0)
        
# If the enemy is off the screen the user wins the game or the Player wins if it collides with the Party prize
    if enemyXPosition < 0 - enemy_width and enemy1XPosition < 0 - enemy1_width and enemy2XPosition < 0 - enemy2_width and enemy3XPosition < 0 - enemy3_width or playerBox.colliderect(prizeBox): 

# Display winning status to the user: 
        print("You win!")
        
# Quit game and exit window: 
        pygame.quit()
        exit(0)

# X and Y positions to approach the player
    enemyXPosition -= 0.35
    enemyYPosition = 2

    enemy1XPosition + 0.30
    enemy1YPosition -=0.20

    enemy2XPosition -= 0.40
    enemy2YPosition += 0.30

    enemy3XPosition = 0.20
    enemy3YPosition -= 0.50

    prizeXPosition -= 0.40
    
    # ================The game loop logic ends here. =============

