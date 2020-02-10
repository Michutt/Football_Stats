import pygame


pygame.init()
win = pygame.display.set_mode((900, 900))

run = True

def Create(win, color1, color2):

    win.fill((255, 255, 255))
    for i in range(10):
        if i % 2 == 0:
            color = color1
        else:
            color = color2
        pygame.draw.circle(win, color, (450, 450), 40 + i * 40, 40)

while run:
    RED = (255, 0, 0)
    YELLOW = (255, 244, 79)
    GREY = (197, 199, 196)
    WHITE = (240, 240, 240)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Create(win, RED, YELLOW)

    pygame.display.update()
    pygame.image.save(win, "firstIMG.png")

    Create(win, GREY, WHITE)

    pygame.display.update()
    pygame.image.save(win, "secondIMG.png")

    run = False

pygame.quit()
