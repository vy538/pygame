import sys, pygame, os

#add this part to become headless
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.environ["SDL_VIDEODRIVER"] = "dummy"
#end of headless
pygame.init()

size = width, height = 3200, 2400
speed = [2, 2]
black = 0, 0, 0

# screen = pygame.display.set_mode(size) #remove for headless
screen = pygame.display.set_mode((1,1)) #ulter for headless

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
bounce = 0
timer = 1
current_time = 0
while current_time<=timer:
    tmp = pygame.time.get_ticks()//1000
    if tmp != current_time:
        current_time = tmp
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    # print(ballrect)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        bounce +=1
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        bounce +=1

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

print('bounce {0} times in {1} sec'.format(bounce,timer))
sys.exit()