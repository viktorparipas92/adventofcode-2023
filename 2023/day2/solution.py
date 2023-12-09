import dataclasses
from collections import defaultdict
from functools import reduce

MAX_BLUE_COUNT = 14
MAX_GREEN_COUNT = 13
MAX_RED_COUNT = 12
MAX_COUNTS = {
    'red': MAX_RED_COUNT,
    'green': MAX_GREEN_COUNT,
    'blue': MAX_BLUE_COUNT,
}


def part_one(filename: str) -> int:
    """
    --- Day 2: Cube Conundrum ---
    You're launched high into the atmosphere! The apex of your trajectory
    just  barely reaches the surface of a large island floating in the sky.
    You gently land in a fluffy pile of leaves. It's quite cold, but you
    don't  see much snow. An Elf runs over to greet you.

    The Elf explains that you've arrived at Snow Island and apologizes for
    the  lack of snow. He'll be happy to explain the situation, but it's a
    bit  of a walk, so you have some time. They don't get many visitors up
    here;  would you like to play a game in the meantime?

    As you walk, the Elf shows you a small bag and some cubes which are
    either  red, green, or blue. Each time you play this game, he will hide
    a secret number of cubes of each color in the bag, and your goal is to
    figure out information about the number of cubes.

    To get information, once a bag has been loaded with cubes, the Elf will
    reach into the bag, grab a handful of random cubes, show them to you,
    and  then put them back in the bag. He'll do this a few times per game.

    You play several games and record the information from each game (your
    puzzle input). Each game is listed with its ID number (like the 11 in
    Game 11: ...) followed by a semicolon-separated list of subsets of cubes
    that were revealed from the bag (like 3 red, 5 green, 4 blue).

    Determine which games would have been possible if the bag had been loaded
     with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the
     sum  of the IDs of those games?
    """
    with open(filename) as file:
        possible_games = 0
        while line := file.readline().strip():
            game = Game(line)
            if game.is_possible():
                possible_games += game.id

    return possible_games


class Game:
    def __init__(self, line: str):
        id_, draws = line.split(':')
        self.id = int(id_.split(' ')[1])

        draws: list = draws.strip().split('; ')
        self.draws: list = [Draw(draw) for draw in draws]

    def is_possible(self) -> bool:
        return all(draw.is_possible() for draw in self.draws)

    @property
    def power(self) -> int:
        """
        Loop through all the draws
        For each draw, find the minimum count for each color
        Multiply the minimum counts together and return the result
        :return:
        """
        min_counts = {}
        for draw in self.draws:
            for cc in draw.cubes:
                if (
                    cc.color not in min_counts
                    or cc.count > min_counts[cc.color]
                ):
                    min_counts[cc.color] = cc.count

        return reduce(lambda x, y: x * y, min_counts.values())



class Draw:
    def __init__(self, line: str):
        cubes_list: list[str] = line.split(', ')
        self.cubes = []
        for cube in cubes_list:
            count, color = cube.split(' ')
            self.cubes.append(CubeCount(color=color, count=int(count)))

    def is_possible(self) -> bool:
        return all(cube_count.is_possible() for cube_count in self.cubes)


@dataclasses.dataclass
class CubeCount:
    color: str
    count: int

    def is_possible(self) -> bool:
        max_color_count = MAX_COUNTS.get(self.color)
        return max_color_count and self.count <= max_color_count


def part_two(filename):
    """
    --- Part Two ---
    The Elf says they've stopped producing snow because they aren't getting
    any water! He isn't sure why the water stopped; however, he can show you
    how to get to the water source to check it out for yourself. It's just
    up ahead!

    As you continue your walk, the Elf poses a second question: in each game
    you played, what is the fewest number of cubes of each color that could
    have been in the bag to make the game possible?

    For each game, find the minimum set of cubes that must have been present.
    What is the sum of the power of these sets?
    """
    with open(filename) as file:
        return sum(Game(line).power for line in file.readlines())


if __name__ == '__main__':
    filename = 'input.txt'
    sum_of_ids = part_one(filename)
    print(sum_of_ids)

    sum_of_power = part_two(filename)
    print(sum_of_power)