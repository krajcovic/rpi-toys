import pygame
import random

pygame.init()
window = pygame.display.set_mode((500, 400))
while True:
    # pygame.draw.rect(window, (255, 0, 0), (0, 0, 50, 50))
    # pygame.display.update()

    # pygame.draw.rect(window, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (100, 100, 50, 50))
    # pygame.draw.rect(window, (0, 255, 0), (200, 150, 50, 50))
    # pygame.draw.rect(window, (0, 0, 255), (300, 200, 50, 50))


    pygame.draw.rect(window, (255, 0, 0), (0, 0, 50, 50))
    # pygame.draw.rect(window, (0,255,0),
    # (40, 0, 50, 50))FROM HERE
    pygame.draw.rect(window, (0, 0, 255), (80, 0, 50, 50))
    pygame.draw.rect(window, (0, 255, 0), (40, 0, 50, 50))
    # TO HERE

    # Just like before to help us remember
    # pygame.draw.circle(WHERE TO DRAW, (RED, GREEN,BLUE), (X COORDINATE, Y COORDINATE), RADIUS, HEIGHT,WIDTH)
    pygame.draw.circle(window, (255, 255, 0), (250, 200), 20, 0)

    pygame.display.update()
