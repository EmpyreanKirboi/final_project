import pygame

import time

import sys

screen = pygame.display.set_mode((400, 400))
screen.fill((0, 0, 255))

while True:
    print("----------check for new events____________")
    recent_events = pygame.event.get()
    print("----------done checking for events--------")
    for event in recent_events:
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                screen.fill((255, 0, 0))
            elif event.key == pygame.K_g:
                screen.fill((0, 255, 0))
            elif event.key == pygame.K_b:
                screen.fill((0, 0, 255))

    pygame.display.flip()
    time.sleep(1)