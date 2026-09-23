import pygame
import settings

pygame.init()

SCREEN = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
DESC = pygame.display.set_caption(settings.CAPTION)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()

