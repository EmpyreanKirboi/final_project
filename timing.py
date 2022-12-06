import pygame
import time
from Delve import i
x = 0
a = pygame.image.load("images/diver_healthy_swim.bmp")
b = pygame.image.load("images/diver_healthy.bmp")
global skin
skin = b
while i>0:
    skin = "a"
    print(skin)
    time.sleep(0.5)
    skin = "b"
    print(skin)
    time.sleep(0.5)
