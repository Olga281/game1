import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption('Шахматная клетка')
    try:
        size = (int(i) for i in input().split())
    except ValueError:
        print('Неправильная форма ввода')
        return -1
    a, b = size
    screen = pygame.display.set_mode(a, a)
    draw(screen)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


def draw(screen):
    screen.fill((0, 0, 0))
    a, b = screen.get_size()
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


if __name__ == '__main__':
    sys.exit(main())






