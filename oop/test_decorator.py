# =============================================================================
# Скрипт для тестирования решений студентов по заданию "Создание декоратора
# класса" (тесты содержат примеры, приведенные в описании задания)
# https://stepik.org/lesson/106937/step/4?unit=81460
# Скопируйте код вашего решения в секцию ВАШ КОД и запустите скрипт
# =============================================================================
from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


# =============================================================================
# начало секции ВАШ КОД
# =============================================================================

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

# =============================================================================
# конец секции ВАШ КОД
# =============================================================================

if __name__ == '__main__':
    # создадим героя
    hero = Hero()
    # проверим правильность характеристик по-умолчанию
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    # проверим список отрицательных эффектов
    assert hero.get_negative_effects() == []
    # проверим список положительных эффектов
    assert hero.get_positive_effects() == []
    # наложим эффект Berserk
    brs1 = Berserk(hero)
    # проверим правильность изменения характеристик
    assert brs1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 22,
                                'Perception': 1,
                                'Endurance': 15,
                                'Charisma': -1,
                                'Intelligence': 0,
                                'Agility': 15,
                                'Luck': 8}
    # проверим неизменность списка отрицательных эффектов
    assert brs1.get_negative_effects() == []
    # проверим, что в список положительных эффектов был добавлен Berserk
    a = brs1.get_positive_effects()
    print(a)
    assert brs1.get_positive_effects() == ['Berserk']
    # повторное наложение эффекта Berserk
    brs2 = Berserk(brs1)
    # наложение эффекта Curse
    cur1 = Curse(brs2)
    # проверим правильность изменения характеристик
    assert cur1.get_stats() == {'HP': 228,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 27,
                                'Perception': -4,
                                'Endurance': 20,
                                'Charisma': -6,
                                'Intelligence': -5,
                                'Agility': 20,
                                'Luck': 13}
    # проверим правильность добавления эффектов в список положительных эффектов
    assert cur1.get_positive_effects() == ['Berserk', 'Berserk']
    # проверим правильность добавления эффектов в список отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # снятие эффекта Berserk
    cur1.base = brs1
    # проверим правильность изменения характеристик
    assert cur1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 20,
                                'Perception': -1,
                                'Endurance': 13,
                                'Charisma': -3,
                                'Intelligence': -2,
                                'Agility': 13,
                                'Luck': 6}
    # проверим правильность удаления эффектов из списка положительных эффектов
    assert cur1.get_positive_effects() == ['Berserk']
    # проверим правильность эффектов в списке отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # проверим незменность характеристик у объекта hero
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    print('All tests - OK!')