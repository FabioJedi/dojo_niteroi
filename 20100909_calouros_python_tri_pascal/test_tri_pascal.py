import unittest

class TestTrianguloPascal(unittest.TestCase):

    def test_triangulo_1_linha(self):
        self.assertEqual(triangulo_pascal(1), [
            [1],
        ])

unittest.main()
