from unittest import TestCase

from day1.solution import part_one, part_two


class TestDay1(TestCase):
    def test_PartOne_TestInput_Return142(self):
        # Arrange
        test_filename = '../test_fixtures/day1_part1.txt'

        # Act
        result = part_one(test_filename)

        # Assert
        self.assertEqual(result, 142)

    def test_PartTwo_TestInput_Return281(self):
        # Arrange
        test_filename = '../test_fixtures/day1_part2.txt'

        # Act
        result = part_two(test_filename)

        # Assert
        self.assertEqual(result, 281)
