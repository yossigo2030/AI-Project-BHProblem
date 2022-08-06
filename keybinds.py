import pygame
import numpy as np

def get_input():
    dir = np.array([0, 0])
    events = pygame.event.get()
    for event in events:
        if event.type != pygame.KEYDOWN:
            continue
        if event.key == pygame.K_LEFT:
            dir -= [1, 0]
        if event.key == pygame.K_RIGHT:
            dir += [1, 0]
        if event.key == pygame.K_UP:
            dir -= [0, 1]
        if event.key == pygame.K_DOWN:
            dir += [0, 1]
    print(dir)
    return dir
