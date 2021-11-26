import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption('Шахматная клетка')
    try:
        a, b = (int(i) for i in input().split())
        if a % b != 0:
            print('a % b != 0')
            return

    except ValueError:
        print('Неправильная форма ввода')
        return -1
    size = a, a
    screen = pygame.display.set_mode(size)
    draw(screen, a, b)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


def draw(screen, a, b):
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


if __name__ == '__main__':
    sys.exit(main())






