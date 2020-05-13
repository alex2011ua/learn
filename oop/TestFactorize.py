def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass

class TestFactorize(unittest.TestCase):
    '''
    test_wrong_types_raise_exception -
    проверяет, что передаваемый в функцию аргумент типа
    float или str вызывает исключение TypeError.
    Тестовый набор входных данных:  'string',  1.5
    '''

    def test_wrong_types_raise_exception(self):
        cases = ("string", 1.5)
        for b in cases:
            with self.subTest(case=b):
                self.assertRaises(TypeError, factorize, b)


    def test_negative(self):
        '''
        test_negative - проверяет, что передача в функцию factorize
        отрицательного числа вызывает исключение ValueError.
        Тестовый набор входных данных:   -1,  -10,  -100
        '''
        cases = (-1, -10, -100)
        for b in cases:
            with self.subTest(case=b):
                self.assertRaises(ValueError, factorize, b)

    def test_zero_and_one_cases(self):
        '''
        test_zero_and_one_cases - проверяет, что при передаче в функцию
         целых чисел 0 и 1, возвращаются соответственно кортежи (0,) и (1,).
        Набор тестовых данных: 0 → (0, ),  1 → (1, )
        '''
        cases = ((0, (0,)),  (1,(1, )))
        for b in cases:
            with self.subTest(case=b):
                a = factorize(b[0])
                self.assertEqual(a, b[1])

    def test_simple_numbers(self):
        ''' что для простых чисел возвращается кортеж, содержащий одно данное число
        Набор тестовых данных: 3 → (3, ),  13 → (13, ),   29 → (29, )'''
        cases = ((3, (3,)), (13, (13,)), (29, (29,)))
        for b in cases:
            with self.subTest(case=b):
                a = factorize(b[0])
                self.assertEqual(a, b[1])

    def test_two_simple_multipliers(self):
        cases = ((6, (2, 3)), (26, (2, 13)), (121, (11, 11)))
        for b in cases:
            with self.subTest(case=b):
                a = factorize(b[0])
                self.assertEqual(a, b[1])
    def test_many_multipliers(self):
        cases = ((1001, (7, 11, 13)), (9699690, (2, 3, 5, 7, 11, 13, 17, 19)))
        for b in cases:
            with self.subTest(case=b):
                a = factorize(b[0])
                self.assertEqual(a, b[1])

