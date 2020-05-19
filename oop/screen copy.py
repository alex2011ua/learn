#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import random
from dataclasses import dataclass
from typing import List

import pygame

SCREEN_DIM = (800, 600)
MAX_SPEED = 10
MIN_SPEED = 1


# =======================================================================================
# Функции для работы с векторами
# =======================================================================================

@dataclass
class Vec2d:
    x: float
    y: float

    def __sub__(self, v: 'Vec2d') -> 'Vec2d':
        """"возвращает разность двух векторов"""
        x1 = self.x - v.x
        x2 = self.y - v.y
        return Vec2d(x1, x2)

    def __add__(self, v: 'Vec2d') -> 'Vec2d':
        """возвращает сумму двух векторов"""
        x1 = self.x + v.x
        x2 = self.y + v.y
        return Vec2d(x1, x2)

    def __len__(self):
        """возвращает длину вектора"""
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __mul__(self, k: float) -> 'Vec2d':
        """возвращает произведение вектора на число"""
        x1 = self.x * k
        x2 = self.y * k
        return Vec2d(x1, x2)

    def int_pair(self):
        """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
        координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
        return self.x, self.y


# =======================================================================================
# Функции отрисовки справочной инфы
# ======================================================================================
def draw_help(game_display_, steps, line_speed):
    """функция отрисовки экрана справки программы"""
    game_display_.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)

    data = list()
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["1 or Num1", "More speed line"])
    data.append(["2 or Num2", "Less speed line"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])
    data.append([str(line_speed), "Line speed"])

    pygame.draw.lines(game_display, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        game_display.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        game_display.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Функции, отвечающие за расчет сглаживания ломаной
# =======================================================================================
class Polyline:

    def __init__(self, game_display_):
        self._steps = 35
        self._line_speed = MIN_SPEED
        self._game_display = game_display_
        self._hue = 0
        self._color = pygame.Color(0)

        self._speeds: List[Vec2d] = list()
        self._base_points: List[Vec2d] = list()
        self._line_points: List[Vec2d] = list()

    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, steps):
        self._steps = steps

    @property
    def line_speed(self):
        return self._line_speed

    @line_speed.setter
    def line_speed(self, line_speed):
        self._line_speed = line_speed

    def add_point(self, point_: Vec2d):
        self._base_points.append(point_)

    def search_base_point(self, point_: Vec2d, search_radius=10):
        """Поиск ближайшей базовой точке
        Поиск производится в области с радиусом 'search_radius' относительно точки 'point_'

        :param point_: relative point
        :param search_radius: search area radius
        :return: point (instead Vec2d) or None
        """
        if point_ in self._base_points:
            return point_

        for p in self._base_points:
            relative_x = point_.x - p.x
            relative_y = point_.y - p.y
            if relative_x * relative_x + relative_y * relative_y <= search_radius * search_radius:
                return p

    def remove_point(self, point_: Vec2d):
        self._base_points.remove(point_)

    def add_speed(self, speed_: Vec2d):
        self._speeds.append(speed_)

    def reset_points(self):
        self._base_points = list()
        self._line_points = list()

    def reset_speeds(self):
        self._speeds = list()

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self._base_points)):
            self._base_points[p] = self._base_points[p] + self._speeds[p]
            if self._base_points[p].x > SCREEN_DIM[0] or self._base_points[p].x < 0:
                self._speeds[p] = Vec2d(- self._speeds[p].x, self._speeds[p].y)
            if self._base_points[p].y > SCREEN_DIM[1] or self._base_points[p].y < 0:
                self._speeds[p] = Vec2d(self._speeds[p].x, -self._speeds[p].y)

    def fill_display(self, *args, **kwargs):
        self._game_display.fill(*args, **kwargs)

        self._hue = (self._hue + 1) % 360
        self._color.hsla = (self._hue, 100, 50, 100)

        return self._color

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        pygame.time.wait(int(5/self.line_speed))  # imitation of speed line

        if style == "line":
            for p_n in range(-1, len(self._line_points) - 1):
                pygame.draw.line(self._game_display, color,
                                 (int(self._line_points[p_n].x), int(self._line_points[p_n].y)),
                                 (int(self._line_points[p_n + 1].x), int(self._line_points[p_n + 1].y)), width)

        elif style == "points":
            for p in self._base_points:
                pygame.draw.circle(self._game_display, color,
                                   (int(p.x), int(p.y)), width)


class Knot(Polyline):

    def set_points(self):
        super().set_points()
        self._line_points = self.get_knot(self._base_points)

    def add_point(self, point_: Vec2d):
        p = super().search_base_point(point_)
        if p is not None:
            super().remove_point(p)
        else:
            super().add_point(point_)
        self._line_points = self.get_knot(self._base_points)

    def get_point(self, points_: List[Vec2d], alpha, deg=None):
        if deg is None:
            deg = len(points_) - 1
        if deg == 0:
            return points_[0]

        return (points_[deg] * alpha) + self.get_point(points_, alpha, deg - 1) * (1 - alpha)

    def get_points(self, base_points: List[Vec2d], count):
        alpha = 1 / count
        return [self.get_point(base_points, i * alpha) for i in range(count)]

    def get_knot(self, points_: List[Vec2d]):
        if len(points_) < 3:
            return []
        res = []
        for i in range(-2, len(points_) - 2):
            ptn: List[Vec2d] = list()

            ptn.append((points_[i] + points_[i + 1]) * 0.5)
            ptn.append(points_[i + 1])
            ptn.append((points_[i + 1] + points_[i + 2]) * 0.5)

            res.extend(self.get_points(ptn, self._steps))
        return res


# =======================================================================================
# Основная программа
# =======================================================================================

if __name__ == "__main__":
    pygame.init()
    game_display = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    knot = Knot(game_display)

    working = True
    show_help = False
    pause = True

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    knot.reset_points()
                    knot.reset_speeds()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    knot.steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    knot.steps -= 1 if knot.steps > 1 else 0
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    knot.line_speed += 1 if knot.line_speed < MAX_SPEED else 0
                if event.key in [pygame.K_2, pygame.K_KP2]:
                    knot.line_speed -= 1 if knot.line_speed > MIN_SPEED else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                knot.add_point(Vec2d(*event.pos))
                knot.add_speed(Vec2d(random.random() * 2, random.random() * 2))
        color = knot.fill_display((0, 0, 0))
        knot.draw_points()
        knot.draw_points(style="line", color=color)
        if not pause:
            knot.set_points()
        if show_help:
            draw_help(game_display, knot.steps, knot.line_speed)

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
