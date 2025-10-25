import dataclasses
import re


def part_one(filename):
    """
    --- Day 3: Gear Ratios ---
    You and the Elf eventually reach a gondola lift station; he says the
    gondola lift will take you up to the water source, but this is as far as
    he can bring you. You go inside.

    It doesn't take long to find the gondolas, but there seems to be a
    problem: they're not moving.

    "Aaah!"

    You turn around to see a slightly-greasy Elf with a wrench and a look of
    surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't
    working right now; it'll still be a while before I can fix it." You offer
    to help.

    The engineer explains that an engine part seems to be missing from the
    engine, but nobody can figure out which one. If you can add up all the part
    numbers in the engine schematic, it should be easy to work out which part
    is missing.

    The engine schematic (your puzzle input) consists of a visual
    representation of the engine. There are lots of numbers and symbols you
    don't really understand, but apparently any number adjacent to a symbol,
    even diagonally, is a "part number" and should be included in your sum.
    (Periods (.) do not count as a symbol.)

    Of course, the actual engine schematic is much larger. What is the sum of
    all of the part numbers in the engine schematic?
    """
    # Read characters from file into a list of lists
    with open(filename) as file:
        lines = file.readlines()

    numbers = []
    for i, line in enumerate(lines):
        number_matches = re.finditer(r'(\d+)', line)
        for number_match in number_matches:
            number = number_match.group()
            start, end = number_match.span()
            numbers.append(Number(int(number), i, start, end))

    symbols = set()
    for i, line in enumerate(lines):
        symbol_matches = re.finditer(r'([^\.\d])', line)
        for symbol_match in symbol_matches:
            symbol = symbol_match.group()
            position: int = symbol_match.start()
            symbols.add(Symbol(symbol, i, position))

    part_numbers = [
        number for number in list(numbers)
        if any(number.is_adjacent(symbol) for symbol in symbols)
    ]

    return sum(pn.number for pn in part_numbers)


@dataclasses.dataclass
class Symbol:
    symbol: str
    line: int
    position: int

    def __hash__(self):
        return hash(self.symbol + str(self.line) + str(self.position))


@dataclasses.dataclass
class Number:
    number: int
    line: int
    start: int
    end: int

    def is_adjacent(self, symbol: Symbol) -> bool:
        return (
            abs(self.line - symbol.line) <= 1
            and self.start - 1 <= symbol.position <= self.end
        )


if __name__ == '__main__':
    filename = 'input.txt'
    sum_of_part_numbers = part_one(filename)
    print(sum_of_part_numbers)
