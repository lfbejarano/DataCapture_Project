import unittest
from Data_Project.DataCapture import DataCapture


class TestStats(unittest.TestCase):
    def test_less(self):
        test = {
            "numbers": (3, 9, 3, 4, 6),
            "input_output": (
                (4, 2),
                (12, 5),
                (3, 0),
                (8, 4),
            )
        }

        stats = self._add_numbers(test["numbers"])
        for input, output in test["input_output"]:
            self.assertEqual(stats.less(input), output)

    def test_greater(self):
        test = {
            "numbers": (3, 9, 3, 4, 6),
            "input_output": (
                (4, 2),
                (12, 0),
                (3, 3),
                (8, 1),
            )
        }

        stats = self._add_numbers(test["numbers"])
        for input, output in test["input_output"]:
            self.assertEqual(stats.greater(input), output)

    def test_between(self):
        test = {
            "numbers": (3, 9, 3, 4, 6),
            "inputs_output": (
                ((3, 6), 4),
                ((5, 9), 2),
                ((4, 8), 2),
                ((1, 10), 5)
            )
        }

        stats = self._add_numbers(test["numbers"])
        for inputs, output in test["inputs_output"]:
            self.assertEqual(stats.between(*inputs), output)

    def _add_numbers(self, numbers):
        temp_DataCapture = DataCapture()
        for number in numbers:
            temp_DataCapture.add(number)
        return temp_DataCapture.build_stats()


if __name__ == '__main__':
    unittest.main()
