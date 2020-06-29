import sys, pygame, os

"""
This is based on the ball example without the screen display
'python3 -m test.py width(optinal) height(optinal)' to test it
it will print out how many times the ball bounce to the wall

ref:
1. ball example:
https://www.pygame.org/docs/tut/PygameIntro.html
2. headless example:
http://www.pygame.org/wiki/HeadlessNoWindowsNeeded
"""

def ballBounce(w=3200,h=2400):

    #add this part to become headless
    os.putenv('SDL_VIDEODRIVER', 'fbcon')
    os.environ["SDL_VIDEODRIVER"] = "dummy"
    #end of headless
    pygame.init()

    size = width, height = w, h
    speed = [2, 2]
    black = 0, 0, 0

    # screen = pygame.display.set_mode(size) #remove for headless
    screen = pygame.display.set_mode((1,1)) #alter for headless

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

    #print out the outcome
    print('screen size: {0},{1}'.format(width,height))
    print('ball size: {0}'.format(ballrect.size))
    print('the ball bounced {0} times in {1} sec'.format(bounce,timer))
    sys.exit()

if len(sys.argv)>1:
    ballBounce(int(sys.argv[1]),int(sys.argv[2]))
else:
    ballBounce()
