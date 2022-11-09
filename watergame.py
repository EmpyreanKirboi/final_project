import pygame

import sys

import time

import itertools

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Game running...")
screen.fill((0, 0, 255))
water_image = pygame.image.load('images/water1.png')
water_rect = water_image.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((10*tile_size, 10*tile_size))
pygame.display.set_caption("Game running...")
screen.fill((0, 0, 255))


screen_rect = screen.get_rect()

rows = screen_rect.height/tile_size
cols = screen_rect.width/tile_size

for x in range(int(rows)):
    for y in range(int(cols)):
        screen.blit(water_image, (x*water_rect.height, y*water_rect.width))

screen.blit(water_image, (168, 168))
screen.blit(water_image, (0, 0))
screen.blit(water_image, (0, 64))
screen.blit(water_image, (64, 0))





screen_rect = screen.get_rect()
screen.blit(water_image, screen_rect.topleft)
screen.blit(water_image, screen_rect.topleft)


while True:
    print("----------check for new events____________")
    recent_events = pygame.event.get()
    print("----------done checking for events--------")
    screen.blit(water_image, (64, 64))

    for event in recent_events:
        if event.type == pygame.QUIT:
            print("I will not quit")
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill((255, 0, 0))
            elif event.key == pygame.K_g:
                screen.fill((0, 255, 0))
            elif event.key == pygame.K_b:
                screen.fill((0, 0, 255))
    pygame.display.flip()
    time.sleep(2)