from unittest import TestCase

from day2.solution import part_one, part_two


class TestDay2(TestCase):
    def test_PartOne_TestInput_Return8(self):
        # Arrange
        test_filename = '../test_fixtures/day2_part1.txt'

        # Act
        result = part_one(test_filename)

        # Assert
        self.assertEqual(8, result)

    def test_PartTwo_TestInput_Return2286(self):
        # Arrange
        test_filename = '../test_fixtures/day2_part1.txt'

        # Act
        result = part_two(test_filename)

        # Assert
        self.assertEqual(2286, result)