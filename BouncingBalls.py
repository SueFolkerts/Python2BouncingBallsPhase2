import random

import pygame
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()
# set the width and height to the size of the screen
size = (width, height) = (screen_info.current_w - 20,screen_info.current_h - 20)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (26, 255, 255)
ball_image = pygame.image.load("ball.png​")
ball_image = pygame.transform.smoothscale(ball_image, (30, 30))
ball_rect = ball_image.get_rect()
ball_rect.center = (width//2, height//2)
speed = pygame.math.Vector2(0, 5)
speed.rotate_ip(random.randint(0, 360))
def move_ball():
    ball_rect.move_ip(speed)
def main():
    while True:
        clock.tick(60)
        move_ball()
        screen.fill(color)
        screen.blit(ball_image, ball_rect)
        pygame.display.flip()



if __name__ == '__main__':
    main()
