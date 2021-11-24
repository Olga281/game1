import pygame

a, b = (int(i) for i in input().split())
size = width, height = (a, a)
screen = pygame.display.set_mode(size)
pygame.init()
pygame.display.set_caption('Шахматная клетка')
screen.fill((0, 0, 0))
n = a // b
y = a
num = 1
while y > 0:
    if num % 2 == 0:
        x = 0
    else:
        x = n
    while x <= a:
        screen.fill(pygame.Color('white'), (x, y - n, n, n))
        x = x + 2 * n
    y = y - n
    num = num + 1


while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
print('Proba')
