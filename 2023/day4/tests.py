from unittest import TestCase

from day4.solution import part_one, part_two


class TestDay4(TestCase):
    def test_PartOne_TestInput_Return13(self):
        # Arrange
        test_filename = '../test_fixtures/day4_part1.txt'

        # Act
        result = part_one(test_filename)

        # Assert
        self.assertEqual(13, result)

    def test_PartTwo_TestInput_Return30(self):
        # Arrange
        test_filename = '../test_fixtures/day4_part2.txt'

        # Act
        result = part_two(test_filename)

        # Assert
        self.assertEqual(30, result)