#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)
FPS = 120
FPS = 50


class Vec2d:
    def __init__(self, x, y, speed_x=None, speed_y=None):
        self.x = x
        self.y = y

        self.speed_x = speed_x
        self.speed_y = speed_y

    def __add__(self, other):
        """возвращает сумму двух векторов"""
        if isinstance(other, Vec2d):
            x = self.x + other.x
            y = self.y + other.y
            return Vec2d(x, y)
        else:
            x = self.x + other
            y = self.y + other
            return Vec2d(x, y)

    def __sub__(self, other):
        if isinstance(other, Vec2d):
            x = self.x - other.x
            y = self.y - other.y
            return Vec2d(x, y)
        else:
            x = self.x - other
            y = self.y - other
            return Vec2d(x, y)

    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        x = self.x * k
        y = self.y * k
        return Vec2d(x, y)

    def lengh(self):
        """возвращает длину вектора"""
        return math.sqrt(self.x * self.x + self.y * self.y)

    def int_pair(self):
        return self.x, self.y


class Polyline:
    def __init__(self):
        self.points = []

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in self.points:
            p.x = p.x + p.speed_x
            p.y = p.y + p.speed_y
            if p.x > SCREEN_DIM[0] or p.x < 0:
                p.speed_x = - p.speed_x
            if p.y > SCREEN_DIM[1] or p.y < 0:
                p.speed_y = - p.speed_y

    def draw_points(self, width=3, color=(255, 255, 255)):
        for p in self.points:
            pygame.draw.circle(gameDisplay, color,
                               (int(p.x), int(p.y)), width)


class Knot(Polyline):
    def __init__(self, poly):
        super().__init__()
        self.points = poly.points

    def get_point(self, base_points, alpha, deg=None):
        if deg is None:
            deg = len(base_points) - 1
        if deg == 0:
            return base_points[0]
        return (base_points[deg] * alpha) + \
               (self.get_point(base_points, alpha, deg - 1) * (1 - alpha))

    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_knot(self, count):
        if len(self.points) < 4:
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)

            res.extend(self.get_points(ptn, count))
        return res

    def draw_points(self, points, width=3, color=(255, 255, 255)):
        for p_n in range(-1, len(points) - 1):
            pygame.draw.line(gameDisplay, color,
                             (int(points[p_n].x), int(points[p_n].y)),
                             (int(points[p_n + 1].x), int(points[p_n + 1].y)),
                             width)



def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["A", "Speed -"])
    data.append(["S", "Speed +"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])
    data.append([str(FPS), "Current speed"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))




if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")
    clock = pygame.time.Clock()
    steps = 4
    working = True
    poliline = Polyline()

    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)


    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    poliline.points = []

                if event.key == pygame.K_s:
                    FPS += 15
                    if FPS >100:
                        FPS = 100
                if event.key == pygame.K_a:
                    FPS -= 20
                    if FPS < 1:
                        FPS = 1
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                a, b = event.pos
                poliline.points.append(Vec2d(a, b, random.random() * 2, random.random() * 2))

        gameDisplay.fill((1, 2, 20))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        poliline.draw_points()

        knot = Knot(poliline)
        list_knot = knot.get_knot(steps)
        knot.draw_points(list_knot, 3, color)
        if not pause:
            poliline.set_points()
        if show_help:
            draw_help()
        clock.tick(FPS)
        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
