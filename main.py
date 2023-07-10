import pygame

pygame.init()
display = pygame.display.set_mode((1280, 720))

fps = pygame.time.Clock()
jogando = True

rect_1 = pygame.Rect(300, 300, 100, 100)

while jogando:

    display.fill((0, 0, 0))
    pygame.draw.rect(display, (255, 255, 255), rect_1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if rect_1.y > 0:
                    rect_1.y -= 5

            if event.key == pygame.K_s:
                if rect_1.y < 620:
                    rect_1.y += 5

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)


    fps.tick(60)
    pygame.display.flip()


