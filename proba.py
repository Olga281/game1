import pygame


def draw(screen, width, a):
    screen.fill((0, 0, 0))
    flag = True
    for y in range(width // a):
        for x in range(width // a):
            if flag:
                color = pygame.Color(0, 0, 0)
                pygame.draw.rect(screen, color, (x * a, y * a, x * a + a, y * a + a), 0)
                flag = False
            else:
                color = pygame.Color(255, 255, 255)
                pygame.draw.rect(screen, color, (x * a, y * a, x * a + a, y * a + a), 0)
                flag = True
        if flag:
            flag = False
        else:
            flag = True


def main():
    try:
        width, a = [int(i) for i in input().split()]
        if width % a != 0:
            print('Не кратно ширине')
            return 1
    except ValueError:
        print('Неправильный формат ввода')
        return 1
    pygame.init()
    screen = pygame.display.set_mode((width, width))
    pygame.display.set_caption('Шахматная клетка')
    draw(screen, width, a)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()


if __name__ == '__main__':
    main()
