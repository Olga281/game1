import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption('Krugi')
    try:
        w, n = (int(i) for i in input().split())

    except ValueError:
        print('Неправильная форма ввода')
        return -1
    d = 2 * w * n
    size = (d, d)
    screen = pygame.display.set_mode(size)
    draw(screen, w, n)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


def draw(screen, w, n):
    screen.fill((0, 0, 0))
    r = w * n
    width = w * n
    color = ['red', 'green', 'blue']
    count = n
    while count > 0:
        pygame.draw.circle(screen, color[(n + count) % 3], (r, r), width)
        width -= w
        count -= 1


if __name__ == '__main__':
    sys.exit(main())