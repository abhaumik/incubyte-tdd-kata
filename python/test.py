import unittest

from add import add


class TestAddFunction(unittest.TestCase):

    # Test simple inputs
    def test_empty_input(self):
        self.assertEqual(add(), 0)

    def test_one_input(self):
        self.assertEqual(add("1"), 1)

    def test_two_inputs(self):
        self.assertEqual(add("1,5"), 6)



if __name__ == "__main__":
    unittest.main()
