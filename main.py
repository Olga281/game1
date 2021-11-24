import pygame

x, y = input().split()
size = width, height = (int(x), int(y))
screen = pygame.display.set_mode(size)
pygame.init()
pygame.display.set_caption('Крест')

def draw():
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), [0, 0], [int(x), int(y)], 5)
    pygame.draw.line(screen, (255, 255, 255), [0, int(y)], [int(x), 0], 5)

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
