# initial imports
import pygame
import time
import random

pygame.init()

#Defining Colours that will be used in the game
black = (0,0,0) # background Color
red = (255, 0, 0) # all sort of alert messages
white = (255,255,255) # colours used for snake
yellow = (255,255, 0) # colors for snake food and score board

size = width, height = 1920, 1080 # defining the size of the Screen

display = pygame.display.set_mode(size) # creating display

clock = pygame.time.Clock() 

block = 20 # defining the size of the snake initially and we will be updating the value of position of the snake as per this value because the width of the snake is initially will not change

#defining  font style
font_style = pygame.font.SysFont(None, 50)

# defining a different font style for the scoreboard
score_font = pygame.font.SysFont('comicsanms',30,italic=True)

#Adding A function to draw 'You Lost' message when the player loses

# defining a function to show and update score on the go
def show_score(score):
    value = score_font.render("Your Score: "+ str(score), True, yellow)
    display.blit(value, [0,0])

# defining a function to send lost or game over message
def send_lost(msg):
    msg = font_style.render(msg, True, red)
    display.blit(msg, [width//2-300, height//2])

#defining a function to update the length of the snake and the position of each block is has and draw it on the go
def snake(snake_list):
    for i in snake_list:
        pygame.draw.rect(display, white, [i[0], i[1], 20, 20])

# defining the main function
def main_loop():

    # below to are two boolean variable to make cases for game over and game close
    game_over = False
    game_close = False

    #initial position for the snake
    x1 = width // 2
    y1 = height // 2

    #updating the direction
    x1_change = 0
    y1_change = 0

    #creating a list to store how many foods the snake has eaten by its length and storing the value of position of each block it contains 
    snake_list = []
    length_of_the_snake = 1 # initial length of the snake

    #creating random position for food
    foodx = round(random.randrange(0,  width - block)/10) * 10
    foody = round(random.randrange(0, height - block)/10) * 10



    while not game_close:
        
        # when the game is over --->
        while game_over == True:
            display.fill(white)
            send_lost("You Lost!! Press ESC to quit or R to restart")
            pygame.display.update()

            # there are two cases if the player want to close the game he/she will press esc or if the player wants to restart he/she will press r
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_close = True
                        game_over  = False
                    if event.key == pygame.K_r:
                        main_loop()
        
        # when the game is being played
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            # keybinding for movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -(block)
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -(block)
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = block
        #case where the snake touches the wall and the game will be over
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change
        display.fill(black)
        #creating food based on the foodx and foody value
        pygame.draw.rect(display, yellow, [foodx, foody, 20, 20])
        #creating a snake head list to store and update the snake positions
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_the_snake:
            del snake_list[0]
        
        #if the snake touches itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        # for continuously updating the snake positions
        snake(snake_list)
        #for continuously updating the score
        show_score(length_of_the_snake - 1)

        pygame.display.update()

        # when the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,  width - block)/10) * 10
            foody = round(random.randrange(0, height - block)/10) * 10
            length_of_the_snake += 1
        
        clock.tick(30)
    pygame.display.update()
    time.sleep(0)


    pygame.quit()
    quit()



main_loop()