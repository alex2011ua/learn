from abc import ABC, abstractmethod


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.base = base

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect, ABC):
    @abstractmethod
    def get_positive_effects(self):
        pass


class AbstractNegative(AbstractEffect, ABC):
    @abstractmethod
    def get_negative_effects(self):
        pass


class Berserk(AbstractPositive):

    def get_stats(self):
        stats = self.base.get_stats()
        stats['HP'] += 50
        stats['Strength'] += 7
        stats['Endurance'] += 7
        stats['Agility'] += 7
        stats['Luck'] += 7
        stats['Perception'] -= 3
        stats['Charisma'] -= 3
        stats['Intelligence'] -= 3
        return stats

    def get_positive_effects(self):
        copy = self.base.get_positive_effects()
        copy.append('Berserk')
        return copy

    ''' Берсерк (Berserk) -

    Увеличивает характеристики: Сила, Выносливость, Ловкость, Удача на 7;
    уменьшает характеристики: Восприятие, Харизма, Интеллект на 3;
    количество единиц здоровья увеличивается на 50.  '''


class Blessing(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()

        stats['Strength'] += 2
        stats['Endurance'] += 2
        stats['Agility'] += 2
        stats['Luck'] += 2
        stats['Perception'] += 2
        stats['Charisma'] += 2
        stats['Intelligence'] += 2
        return stats

    def get_positive_effects(self):
        copy = self.base.get_positive_effects()
        copy.append('Blessing')
        return copy
    ''' Благословение (Blessing) -
    увеличивает все основные характеристики на 2.
      Сила (Strength), 
      Восприятие (Perception), 
      Выносливость (Endurance), 
      Харизма (Charisma), 
      Интеллект (Intelligence), 
      Ловкость (Agility), 
      Удача (Luck)'''


class Weakness(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] -= 4
        stats['Endurance'] -= 4
        stats['Agility'] -= 4

        return stats

    def get_negative_effects(self):
        copy = self.base.get_negative_effects()
        copy.append('Weakness')
        return copy
    ''' Слабость (Weakness) -

    уменьшает характеристики: Сила, Выносливость, Ловкость на 4.  '''


class Curse(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] -= 2
        stats['Endurance'] -= 2
        stats['Agility'] -= 2
        stats['Luck'] -= 2
        stats['Perception'] -= 2
        stats['Charisma'] -= 2
        stats['Intelligence'] -= 2
        return stats

    def get_negative_effects(self):
        copy = self.base.get_negative_effects()
        copy.append('Curse')
        return copy
    ''' Проклятье (Curse) -

    уменьшает все основные характеристики на 2.  '''


class EvilEye(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Luck'] -= 10
        return stats

    def get_negative_effects(self):
        copy = self.base.get_negative_effects()
        copy.append('EvilEye')
        return copy
