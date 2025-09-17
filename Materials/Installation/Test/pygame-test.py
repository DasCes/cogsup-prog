#! /usr/bin/env python
# Time-stamp: <2021-03-02 12:34:13 christophe@pallier.org>

""" Hering illusion demo.

    See https://sites.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
"""

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

W, H = 1000, 700  # Size of the graphic window

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption("Hering illusion")

done = False
while not done:
    screen.fill(WHITE)
    
    # Vertical red lines
    for dx in (-60, 60):
        pygame.draw.line(screen, RED, (W // 2 + dx, 0), (W // 2 + dx, H), 3)
    pygame.display.flip()
    pygame.time.wait(2000)
    
    # Background black lines
    for x in range(-W // 3, 4 * W // 3, 30):
        pygame.draw.line(screen, BLACK, (x, 0), (W - x, H), 1)
    pygame.display.flip()
    pygame.time.wait(2000)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()