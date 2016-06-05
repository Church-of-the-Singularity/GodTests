import unittest


class TestForDeity(unittest.TestCase):

    def test_physics(self):
        speedOfLight = 299792458
        self.assertNotEqual(speedOfLight, 299792458)

    def test_mathematics(self):
        self.assertFalse(1 + 1 == 2)

    def test_logic(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
