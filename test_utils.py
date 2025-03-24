import unittest
from utils import is_prime, multiplicar, dividir, cubic, say_hello

class TestUtils(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(0))  # Corrección aquí, debe ser False
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertEqual(is_prime(-5), "Os números negativos non están permitidos")

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)
        self.assertEqual(multiplicar(-1, 5), -5)
        self.assertEqual(multiplicar(0, 10), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        with self.assertRaises(ValueError):
            dividir(5, 0)

    def test_cubic(self):
        self.assertEqual(cubic(3), 27)
        self.assertEqual(cubic(0), 0)
        self.assertEqual(cubic(-2), -8)

    def test_say_hello(self):
        self.assertEqual(say_hello("Carlos"), "Ola, Carlos")
        self.assertEqual(say_hello("Ana"), "Ola, Ana")

if __name__ == '__main__':
    unittest.main()
