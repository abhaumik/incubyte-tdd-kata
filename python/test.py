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

    # Test for any size of string input
    def test_various_sizes(self):
        test_cases = [
            (','.join(['1'] * numberOfInputs), numberOfInputs) for numberOfInputs in [0, 1, 2, 3, 5, 10, 100]
        ]

        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                self.assertEqual(add(input_str), expected)

    # Test for delimiters
    def test_newline_delimiter(self):
        self.assertEqual(add("1\n2,3"), 6)


if __name__ == "__main__":
    unittest.main()
