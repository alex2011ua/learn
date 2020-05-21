#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vec):
        """Return sum of two vectors"""
        return Vec2d(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        """Return difference between two vectors"""
        return Vec2d(self.x - vec.x, self.y - vec.y)

    def __mul__(self, k):
        """Return product of vector by number"""
        return Vec2d(self.x * k, self.y * k)

    def __len__(self):
        """Return length of vector"""
        return math.sqrt(self.x**2 + self.y**2)

    def int_pair(self):
        """Return coordinates of vector in integer format"""
        return int(self.x), int(self.y)


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def __len__(self):
        return len(self.points)

    def add_point(self, point):
        """Add point to polyline with specified coordinates 
        and random speed for each coordinates of point"""
        self.points.append(point)
        speed = random.random() - 0.5, random.random() - 0.5
        self.speeds.append(Vec2d(*speed))

    def del_point(self):
        """Remove last point"""
        self.points.pop()
        self.speeds.pop()

    def set_points(self, gameDisplay, speed=1):
        """Recalculate points coordinates based on specified speed
        and borders of graphic window"""
        borders = gameDisplay.get_size()
        for i in range(len(self.points)):
            self.points[i] += self.speeds[i] * speed
            if self.points[i].x > borders[0] or self.points[i].x < 0:
                self.speeds[i].x = -self.speeds[i].x
            if self.points[i].y > borders[1] or self.points[i].y < 0:
                self.speeds[i].y = -self.speeds[i].y

    def draw_points(self, gameDisplay, color=(255,255,255), width=3):
        """Draw points on screen with specified color and width"""
        for p in self.points:
            pygame.draw.circle(gameDisplay, color, p.int_pair(), width)

    def draw_lines(self, gameDisplay, color=(127,127,127), width=1):
        """Connect points with lines on screen with specified 
        color and width"""
        for i in range(len(self.points)):
            pygame.draw.line(gameDisplay, color, 
                             self.points[i-1].int_pair(), 
                             self.points[i].int_pair(), width)

    def clear_points(self):
        """Remove all points from polyline"""
        self.points.clear()


class Knot(Polyline):
    def __init__(self):
        self.points = []
        self.speeds = []
        self.curve = []

    def add_point(self, point, steps):
        """Add base point and calculate points of curve"""
        super().add_point(point)
        self.get_knot(steps)

    def set_points(self, gameDisplay, steps=10, speed=1):
        """Recalculate coordinates of base points and 
        calculate points of curve"""
        super().set_points(gameDisplay, speed)
        self.get_knot(steps)

    def del_point(self, steps):
        """Remove last base point and calculate points of curve"""
        super().del_point()
        self.get_knot(steps)

    def draw_lines(self, gameDisplay, color=(127,127,127), width=3):
        """Draw curve on screen with specified color and width"""
        for i in range(len(self.curve)):
            pygame.draw.line(gameDisplay, color, 
                             self.curve[i-1].int_pair(), 
                             self.curve[i].int_pair(), width)

    def get_knot(self, steps):
        """Calculate curve points based on base points"""
        self.curve = []
        pts = self.points
        if len(pts) < 3: return
        for i in range(-2, len(pts)-2):
            ptn = []
            ptn.append((pts[i] + pts[i+1]) * 0.5)
            ptn.append(pts[i+1])
            ptn.append((pts[i+1] + pts[i+2]) * 0.5)
            self.curve.extend(self.get_points(ptn, steps))

    def get_points(self, base_points, steps):
        alpha = 1 / steps
        res = []
        for i in range(steps):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha \
                + self.get_point(points, alpha, deg - 1) * (1 - alpha)


class Menu:
    def __init__(self, data):
        self.data = [
            ("F1", "Show/Hide Help"), 
            ("R", "Restart"), 
            ("P", "Pause/Play"), 
            ("N", "Begin new knot"),
            ("Mouse", "Add base point"),
            ("D", "Delete last base point"),
            ("H", "Hide/Show base points"),
            ("Num+", "More curve points"), 
            ("Num-", "Less curve points"), 
            ("\u2191", "Speed up"), 
            ("\u2193", "Speed down"), 
            ("", "")] + data
        self.font = [pygame.font.SysFont("courier", 24), 
                     pygame.font.SysFont("serif", 24)]

    def show_menu(self, gameDisplay):
        gameDisplay.fill((50, 50, 50))
        pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, 
            [(0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(self.data):
            gameDisplay.blit(self.font[0].render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            gameDisplay.blit(self.font[1].render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# ============
# Main program
# ============

if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("SuperScreenSaver")

    knots = [Knot()]
    menu = Menu([("", ""), ("", "")])

    pause = True
    working = True
    show_help = False
    hide_points = False

    speed = 3
    steps = 10
    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                knots[-1].add_point(Vec2d(*event.pos), steps)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    knots.clear()
                    knots.append(Knot())
                    hide_points = False
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1 if steps < 20 else 0
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0
                if event.key == pygame.K_UP:
                    speed += 1 if speed < 10 else 0
                if event.key == pygame.K_DOWN:
                    speed -= 1 if speed > 1 else 0
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_d:
                    knots[-1].del_point(steps)
                if event.key == pygame.K_h:
                    hide_points = not hide_points
                if event.key == pygame.K_n:
                    knots.append(Knot())

        gameDisplay.fill((0, 0, 0))
        hue += 0.1
        for i, knot in enumerate(knots):
            color.hsla = ((hue + i * 360 / len(knots)) % 360, 50, 50, 50)
            knot.draw_lines(gameDisplay, color)
            if not hide_points:
                knot.draw_points(gameDisplay)
            if not pause:
                knot.set_points(gameDisplay, steps, speed)
            else:
                knot.get_knot(steps)

        if show_help:
            menu.data[-2] = (str(steps), "Curve points (1 - 20)")
            menu.data[-1] = (str(speed), "Current speed (1 - 10)")
            menu.show_menu(gameDisplay)

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
