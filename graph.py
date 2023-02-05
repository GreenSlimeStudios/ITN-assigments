import pygame
import math

pygame.init()
window = pygame.display.set_mode((600, 300))

def fun(x):
    return (abs(x)*2-3)*(abs(x)*2-2)*(abs(x)*2-4)*abs(x)*2*(math.sqrt(abs(x))/12)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)

    for i in range(0,300):
        window.set_at((300, i), (255, 255, 255))


    for i in range(-300, 300):
        x = i/100
        y = fun(x)
        window.set_at((300+i, 150 + int(round(y*100))), (255, 255, 255))
        window.set_at((300 + i, 150), (255, 255, 255))
    # window.set_at((i, int(round(y))), (255,255,255))  150+int(round(y))*100),

    pygame.display.flip()

pygame.quit()
exit()
