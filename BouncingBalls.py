import sys
import pygame
from pygame.locals import *

# NEW FOLLOWS ********************
import random
# NEW ABOVE **********************

pygame.init()
screen_info = pygame.display.Info()

# set the width and height to the size of the screen
size = (width, height) = (screen_info.current_w - 20,screen_info.current_h - 20)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (26, 255, 255)

# NEW FOLLOWS **************************************************************************************
ball_image = pygame.image.load("ball.png")
    #pygame.image.load("C:\\Users\\Sue\\PycharmProjects\\Python2BouncingBallsPhase2\\ball.png​")
ball_image = pygame.transform.smoothscale(ball_image, (30, 30))
ball_rect = ball_image.get_rect()
ball_rect.center = (width//2, height//2)
speed = pygame.math.Vector2(0, 5)
speed.rotate_ip(random.randint(0, 360))

def move_ball():
    ball_rect.move_ip(speed)
# NEW ABOVE ***************************************************************************************

def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        screen.fill(color)

# NEW FOLLOWS **************************************************************************************
        move_ball()
        screen.blit(ball_image, ball_rect)
# NEW ABOVE ***************************************************************************************

        pygame.display.flip()



if __name__ == '__main__':
    main()
