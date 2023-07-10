import pygame

pygame.init()
display = pygame.display.set_mode((1280, 720))

fps = pygame.time.Clock()
jogando = True

rect_1 = pygame.Rect(0, 0, 200, 200)
rect_2 = pygame.Rect(1080, 0, 200, 200)
rect_3 = pygame.Rect(1080, 520, 200, 200)
rect_4 = pygame.Rect(0, 520, 200, 200)




while jogando:

    display.fill((0, 0, 0))
    pygame.draw.rect(display, (0, 255, 255), rect_1)
    pygame.draw.rect(display, (255, 0, 0), rect_2)
    pygame.draw.rect(display, (183, 0, 255), rect_3)
    pygame.draw.rect(display, (0, 255, 179), rect_4)

    pygame.draw.circle(display, (0, 80, 84), (300, 300), 50)
    pygame.draw.circle(display, (89, 185, 212), (400, 500), 100)
    pygame.draw.circle(display, (55, 44, 145), (800, 550), 150)

    fps.tick(60)
    pygame.display.flip()


