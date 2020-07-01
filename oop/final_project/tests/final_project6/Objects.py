from abc import ABC, abstractmethod
import pygame
import random
import numpy as np
import Service


def create_sprite(img, sprite_size):
    icon = pygame.image.load(img).convert_alpha()
    icon = pygame.transform.scale(icon, (sprite_size, sprite_size))
    sprite = pygame.Surface((sprite_size, sprite_size), pygame.HWSURFACE)
    sprite.blit(icon, (0, 0))
    return sprite


class Interactive(ABC):

    @abstractmethod
    def interact(self, engine, hero):
        pass


class AbstractObject(ABC):
    def __init__(self, position, icon):
        self.position = position
        self.sprite = icon

    def draw(self, display):
        sprite_size, w, h = display.game_engine.sprite_size, display.get_width(), display.get_height()

        x_threshold = int(0.6*w/sprite_size)
        y_threshold = int(0.6*h/sprite_size)
        
        if self.position[0] > 36:
            min_x = 36 - x_threshold
        elif self.position[0] > x_threshold:
            min_x = self.position[0] - x_threshold
        else:
            min_x = 0

        
        if self.position[1] > 37:
            min_y = 37 - y_threshold
        elif self.position[1] > y_threshold:
            min_y = self.position[1] - y_threshold
        else:
            min_y = 0

        display.blit(self.sprite, ((self.position[0] - min_x)*sprite_size, (self.position[1] - min_y)*sprite_size))


class Ally(AbstractObject, Interactive):

    def __init__(self, icon, action, position):
        self.sprite = icon
        self.action = action
        self.position = position

    def interact(self, engine, hero):
        self.action(engine, hero)


class Creature(AbstractObject):

    def __init__(self, icon, stats, position):
        self.sprite = icon
        self.stats = stats
        self.position = position
        self.calc_max_HP()
        self.hp = self.max_hp

    def calc_max_HP(self):
        self.max_hp = 5 + self.stats["endurance"] * 2


class Hero(Creature):

    def __init__(self, stats, icon):
        pos = [1, 1]
        self.level = 1
        self.exp = 0
        self.gold = 0
        super().__init__(icon, stats, pos)

    def level_up(self):
        while self.exp >= 100 * (2 ** (self.level - 1)):
            yield "level up!"
            self.level += 1
            self.stats["strength"] += 2
            self.stats["endurance"] += 2
            self.calc_max_HP()
            self.hp = self.max_hp


class Enemy(Creature, Interactive):
    def __init__(self, icon, prop, exp, position):
        self.sprite = icon
        self.prop = prop
        self.position = position
        self.exp = exp
        self.stats = prop
        self.calc_max_HP()
        self.hp = self.max_hp

    def interact(self, engine, hero):
        hero.hp -= int(self.stats['strength']/hero.stats['endurance'])
        self.hp -= int(hero.stats['strength']/self.stats['endurance'])
        hero.exp += self.exp/100


    def move(self, engine):
        def up():
            if engine.map[self.position[1] - 1][self.position[0]] == Service.wall:
                return
            self.position = (self.position[0], self.position[1] - 1)
        
        def down():
            if engine.map[self.position[1] - 1][self.position[0]] == Service.wall:
                return
            self.position = (self.position[0], self.position[1] - 1)
        
        def left():
            if engine.map[self.position[1]][self.position[0] - 1] == Service.wall:
                return
            self.position = (self.position[0] - 1, self.position[1])
        
        def right():
            if engine.map[self.position[1]][self.position[0] + 1] == Service.wall:
                return
            self.position = (self.position[0] + 1, self.position[1])

        actions = [
            left, right, up, down
        ]
        answer = np.random.randint(0, 100, 4)
        actions[np.argmax(answer)]()


class Effect(Hero):

    def __init__(self, base):
        self.base = base
        self.stats = self.base.stats.copy()
        self.apply_effect()

    @property
    def position(self):
        return self.base.position

    @position.setter
    def position(self, value):
        self.base.position = value

    @property
    def level(self):
        return self.base.level

    @level.setter
    def level(self, value):
        self.base.level = value

    @property
    def gold(self):
        return self.base.gold

    @gold.setter
    def gold(self, value):
        self.base.gold = value

    @property
    def hp(self):
        return self.base.hp

    @hp.setter
    def hp(self, value):
        self.base.hp = value

    @property
    def max_hp(self):
        return self.base.max_hp

    @max_hp.setter
    def max_hp(self, value):
        self.base.max_hp = value

    @property
    def exp(self):
        return self.base.exp

    @exp.setter
    def exp(self, value):
        self.base.exp = value

    @property
    def sprite(self):
        return self.base.sprite

    @abstractmethod
    def apply_effect(self):
        pass


class Berserk(Effect):
    def apply_effect(self):
        for key in ['strength', 'endurance', 'luck']:
            self.stats[key] += 7
        self.hp += 50


class Blessing(Effect):
    def apply_effect(self):
        for key in ['strength', 'endurance', 'luck', 'intelligence']:
            self.stats[key] += 2


class Weakness(Effect):
    def apply_effect(self):
        for key in ['strength', 'endurance']:
            self.stats[key] -= 4