import pygame
from sys import exit
from pygame.locals import *
import math


class Brush():

    def __init__(self, surface, size, color):
        self.surface = surface
        self.size = size
        self.color = color
        self.brush = []
        self.brush_num = 0
        self.pos = -1

    def draw(self):
        for i in self.brush:
            color = i[0]
            size = i[1]
            for w in i[2:]:
                pygame.draw.circle(self.surface, color, w, size)

    def set_brush(self):
        if len(self.brush[self.brush_num]) > 1:
            last_pos = self.brush[-1][-1]
            points = [last_pos]
            len_x = self.pos[0] - last_pos[0]
            len_y = self.pos[1] - last_pos[1]
            length = math.sqrt(len_x ** 2 + len_y ** 2)
            if length:
                step_x = len_x / length
                step_y = len_y / length
                for i in range(int(length)):
                    points.append(
                        (points[-1][0] + step_x, points[-1][1] + step_y))
                points = map(lambda x: (
                    int(0.5 + x[0]), int(0.5 + x[1])), points)
                self.brush[-1].extend(points)


class Painter():

    def __init__(self, size, color):
        self.size = size
        self.background = color
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.background)

    def reset(self):
        self.surface.fill(self.background)


def quit():
    pygame.quit()
    exit()


def main():

    small = pygame.image.load('painter/small.png')
    big = pygame.image.load('painter/big.png')
    pen1 = pygame.image.load('painter/pen1.png')
    pen2 = pygame.image.load('painter/pen2.png')
    pen1_rect = pen1.get_rect()
    pen2_rect = pen2.get_rect()
    pen1_rect.centerx, pen1_rect.top = 60, 20
    pen2_rect.centerx, pen2_rect.top = 60, 100
    small_rect = small.get_rect()
    big_rect = big.get_rect()
    small_rect.centerx, small_rect.top = 40, 190
    big_rect.centerx, big_rect.top = 80, 190

    color_rect = []
    brush_color = [
        (0xff, 0x00, 0xff), (0x80, 0x00, 0x80),
        (0x00, 0x00, 0xff), (0x00, 0x00, 0x80),
        (0x00, 0xff, 0xff), (0x00, 0x80, 0x80),
        (0x00, 0xff, 0x00), (0x00, 0x80, 0x00),
        (0xff, 0xff, 0x00), (0x80, 0x80, 0x00),
        (0xff, 0x00, 0x00), (0x80, 0x00, 0x00),
        (0xc0, 0xc0, 0xc0), (0x80, 0x80, 0x80),
        (0xff, 0xff, 0xff), (0x00, 0x00, 0x00),
    ]

    c = 0
    d = 16
    b = 0

    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption('Painter')
    painter = Painter((900, 600), (255, 255, 255))
    brush = Brush(screen, 1, (0, 0, 0))
    clock = pygame.time.Clock()
    is_draw = False

    m_rect = pygame.Rect((0, 0, 125, 600))
    brush_img = pen1
    brush_img_rect = brush_img.get_rect()
    visible = False

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    brush.size += 1
                elif event.key == K_DOWN:
                    if brush.size == 1:
                        brush.size = 1
                    else:
                        brush.size -= 1
                elif event.key == K_SPACE:
                    brush.brush.clear()
                    brush.brush_num = 0
                elif event.key == K_BACKSPACE:
                    if brush.brush_num:
                        brush.brush.pop()
                        brush.brush_num -= 1
                elif event.key == K_F1:
                    brush.surface = painter.surface
                    brush.draw()
                    pygame.image.save(painter.surface, 'My creation.png')
                    brush.surface = screen
                    painter.reset()
            elif event.type == MOUSEBUTTONDOWN:
                is_draw = True
                brush.brush.append([brush.color, brush.size, event.pos])
                for i in color_rect:
                    if event.button == 1 and i.collidepoint(event.pos):
                        brush.color = brush_color[b]
                    b += 1
                b = 0
                if event.button == 1 and pen1_rect.collidepoint(event.pos):
                    brush_img = pen1
                    brush.size = 1
                elif event.button == 1 and pen2_rect.collidepoint(event.pos):
                    brush_img = pen2
                    brush.size = 4
                elif event.button == 1 and small_rect.collidepoint(event.pos):
                    if brush.size == 1:
                        brush.size = 1
                    else:
                        brush.size -= 1
                elif event.button == 1 and big_rect.collidepoint(event.pos):
                    brush.size += 1
            elif event.type == MOUSEBUTTONUP:
                is_draw = False
                brush.brush_num += 1
            elif event.type == MOUSEMOTION and is_draw:
                brush.pos = event.pos
                brush.set_brush()
            if event.type == MOUSEMOTION:
                if m_rect.collidepoint(event.pos):
                    pygame.mouse.set_visible(True)
                    visible = True

                else:
                    pygame.mouse.set_visible(False)
                    visible = False

        screen.fill((255, 255, 255))
        brush.draw()
        pygame.draw.rect(screen, (205, 205, 205,), (0, 0, 125, 600))
        screen.blit(pen1, pen1_rect)
        screen.blit(pen2, pen2_rect)
        screen.blit(small, small_rect)
        screen.blit(big, big_rect)
        for i in brush_color:
            xy = -1
            if c % 2:
                xy = (60, 20 * c + 230, 42, 42)
            else:
                xy = (20, 20 * c + 250, 40, 40)
            rect = pygame.draw.rect(screen, i, xy)
            c += 1
            if d > 0:
                color_rect.append(rect)
                d -= 1
        c = 0
        if not visible:
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(brush_img, (mouse_pos[0], mouse_pos[
                        1] - brush_img_rect.height))
        pygame.display.flip()
        clock.tick(120)
if __name__ == '__main__':
    main()
