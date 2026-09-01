import unittest


def test_function(value):
    return value * 20

def sum_two_values(a, b):
    return a + b

def power(x, n):
    return x ** n

def concat_values(*args):
    result = ''
    for item in args:
        result += str(item)
    return result


def desc(x, y):
    if y == 0:
        raise ValueError('should not be equal 0')
    return x / y

class UserTestCase(unittest.TestCase):

    def test_01_sum(self):
        """тестуємо сумму доданків"""
        self.assertEqual(2 + 2, 4)

    def test_02_multiply(self):
        """тест множення"""
        # A 
        multiply_a = 2
        multiply_b = 4
        expected_result = 8
        # Action
        multiply_result = multiply_a * multiply_b
        # assert
        self.assertTrue(multiply_result == expected_result, f"We multiply {multiply_a} * {multiply_b} ang get {multiply_result}, but expected is {expected_result}")

    def test_03_function(self):
        value = 100
        expected_result = value * 20
        self.assertEqual(test_function(value), expected_result)

    def test_04_sum_two_values(self):
        value1 = 10
        value2 = 20
        result = sum_two_values(value1, value2)
        self.assertEqual(result, value1 + value2)

    def test_05_power(self):
        value = 2
        st = 8
        result = power(value, st)
        expected_value = value ** st
        self.assertEqual(result, expected_value)

    def test_06_concat_values(self):
        values = 1, 2, 3, 4
        result = concat_values(*values)
        expected_result = '1234'
        self.assertEqual(result, expected_result)

    def test_07_desc(self):
        x, y = 20, 10
        result = desc(x, y)
        expected_result = 2.0
        self.assertEqual(result, expected_result)

    def test_07_desc_with_zero(self):
        with self.assertRaises(ValueError):
            desc(20, 0)

unittest.main(verbosity=2)