#initial imports for pygame
import sys, pygame

# to initialize pygame window we need to call the below function
pygame.init()

# defining the size of the window
size = width, height = 1920, 1080

# definig the speed of the ball in integer
speed = [12, 12]

# defining black color for background in RGB
black = 0,0,0

#defining pygame screen with predefined size
screen = pygame.display.set_mode(size)

#creating an object of ball with a picture
ball = pygame.image.load("intro_ball.gif")

#defining the rectangular part covering the ball
ballhitbox = ball.get_rect()

#below is the main loop for the game to run

#creating a variable named 'running' to use in the while loop for the loop to running unless we are forcing the function to quit
running = 1

while running:
    # getting any events such as mouse click
    for event in pygame.event.get():
        #defining when the pygame must  stop for this case it is the top right close button
        if event.type == pygame.QUIT:
            sys.exit()
    
    # updating ballhitbox when its moving
    ballhitbox = ballhitbox.move(speed)
    #defining edge cases when the ball bounces
    if ballhitbox.left < 0 or ballhitbox.right > width:
        speed[0] = -speed[0]
    if ballhitbox.top < 0 or  ballhitbox.bottom > height:
        speed[1] = -speed[1]
    
    #filling the sceen with the background color black
    screen.fill(black)
    #sceen starts drawing
    screen.blit(ball, ballhitbox)
    pygame.display.flip()