import unittest

from add import add


class TestAddFunction(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(add(), 0)


if __name__ == "__main__":
    unittest.main()
