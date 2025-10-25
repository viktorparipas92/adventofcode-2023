from unittest import TestCase

from day3.solution import part_one


class TestDay3(TestCase):
    def test_PartOne_TestInput_Return4361(self):
        # Arrange
        test_filename = '../test_fixtures/day3_part1.txt'

        # Act
        result = part_one(test_filename)

        # Assert
        self.assertEqual(4361, result)