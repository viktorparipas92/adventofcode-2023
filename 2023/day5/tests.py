from unittest import TestCase

from day5.solution import part_one


class TestDay5(TestCase):
    def test_PartOne_TestInput_Return35(self):
        # Arrange
        test_filename = '../test_fixtures/day5_part1.txt'

        # Act
        result = part_one(test_filename)

        # Assert
        self.assertEqual(35, result)