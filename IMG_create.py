import pygame


pygame.init()
win = pygame.display.set_mode((800, 800))

run = True

def Create(win, color1, color2):

    win.fill((255, 255, 255))
    for i in range(10):
        if i % 2 == 0:
            color = color1
        else:
            color = color2
        pygame.draw.circle(win, color, (400, 400), 30 + i * 30, 30)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Create(win, (200, 0, 0), (200, 200, 0))

    pygame.display.update()
    pygame.image.save(win, "firstIMG.jpg")

    Create(win, (50, 0, 0), (200, 200, 200))

    pygame.display.update()
    pygame.image.save(win, "secondIMG.jpg")

    run = False

pygame.quit()
