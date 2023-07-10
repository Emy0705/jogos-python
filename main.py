import pygame

pygame.init()
display = pygame.display.set_mode((1280, 720))

fps = pygame.time.Clock()
jogando = True


while jogando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(display, (255, 255, 255), event.pos, 50)







    fps.tick(60)
    pygame.display.flip()