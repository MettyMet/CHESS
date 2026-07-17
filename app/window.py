# pyrefly: ignore [missing-import]
import pygame
import const
pygame.init()


screen = pygame.display.set_mode((const.WIDTH_WINDOW, const.HEIGHT_WINDOW))
pygame.display.set_caption("CHESS")
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()