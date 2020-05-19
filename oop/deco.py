class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points

            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect:
    def __init__(self, obj):
        self.obj = obj


class AbstractPositive(AbstractEffect):
    pass


class AbstractNegative(AbstractEffect):
    pass


class Berserk(AbstractPositive):
    pass
    ''' Берсерк (Berserk) -

    Увеличивает характеристики: Сила, Выносливость, Ловкость, Удача на 7;
    уменьшает характеристики: Восприятие, Харизма, Интеллект на 3;
    количество единиц здоровья увеличивается на 50.  '''


class Blessing(AbstractPositive):
    pass
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
    pass
    ''' Слабость (Weakness) -

    уменьшает характеристики: Сила, Выносливость, Ловкость на 4.  '''


class Curse(AbstractNegative):
    pass
    ''' Проклятье (Curse) -

    уменьшает все основные характеристики на 2.  '''


class EvilEye(AbstractNegative):
    pass


''' Сглаз (EvilEye) -

    уменьшает  характеристику Удача на 10.  '''


'''
абстрактные классы AbstractPositive,  AbstractNegative и соответственно их потомки 
могут принимать любой параметр base при инициализации объекта (_ _ init _ _ (self, base))

'''
'''
>>> from deco import *
>>> # создаем героя
>>> hero = Hero()
>>> hero.get_stats()
{'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8, 'Charisma': 2, 'Intelligence': 3, 'Agility': 8, 'Luck': 1}
>>> hero.stats
{'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8, 'Charisma': 2, 'Intelligence': 3, 'Agility': 8, 'Luck': 1}
>>> hero.get_negative_effects()
[ ]
>>> hero.get_positive_effects()
[ ]
>>> # накладываем эффект

>>> brs1 = Berserk(hero)
>>> brs1.get_stats()
{'HP': 178, 'MP': 42, 'SP': 100, 'Strength': 22, 'Perception': 1, 'Endurance': 15, 'Charisma': -1, 'Intelligence': 0, 'Agility': 15, 'Luck': 8}
>>> brs1.get_negative_effects()
[ ]
>>> brs1.get_positive_effects()
['Berserk']

>>> # накладываем эффекты
>>> brs2 = Berserk(brs1)

>>> cur1 = Curse(brs2)

>>> cur1.get_stats()
{'HP': 228, 'MP': 42, 'SP': 100, 'Strength': 27, 'Perception': -4, 'Endurance': 20, 'Charisma': -6, 'Intelligence': -5, 'Agility': 20, 'Luck': 13}
>>> cur1.get_positive_effects()
['Berserk', 'Berserk']
>>> cur1.get_negative_effects()
['Curse']
>>> # снимаем эффект Berserk
>>> cur1.base = brs1
>>> cur1.get_stats()
{'HP': 178, 'MP': 42, 'SP': 100, 'Strength': 20, 'Perception': -1, 'Endurance': 13, 'Charisma': -3, 'Intelligence': -2, 'Agility': 13, 'Luck': 6}
>>> cur1.get_positive_effects()
['Berserk']
>>> cur1.get_negative_effects()
['Curse']

>>>
'''