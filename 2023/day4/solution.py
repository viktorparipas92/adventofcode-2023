import re


class Card:
    def __init__(self, line: str):
        """
        Parse a card from a line of text.

        :param line: the line of text to parse
        """
        card_id, line = line.strip().split(': ')
        self.card_number = re.search(r'(\d+)', card_id).group()

        winning_numbers, your_numbers = line.split(' | ')
        self.winning_numbers = {
            int(number) for number in winning_numbers.split()
        }

        self.your_numbers = [
            int(number) for number in your_numbers.split()
        ]

    def __repr__(self):
        return f'Card({self.winning_numbers}, {self.your_numbers})'

    def __str__(self):
        return self.__repr__()

    def evaluate(self):
        matches = sum(
            1 for yn in self.your_numbers if yn in self.winning_numbers
        )
        return 2 ** (matches - 1) if matches else 0




def part_one(filename):
    """
    --- Day 4: Scratchcards ---
    The gondola takes you up. Strangely, though, the ground doesn't seem to
    be coming with you; you're not climbing a mountain. As the circle of Snow
    Island recedes below you, an entire new landmass suddenly appears above
    you! The gondola carries you to the surface of the new island and lurches
    into the station.

    As you exit the gondola, the first thing you notice is that the air here
    is much warmer than it was on Snow Island. It's also quite humid. Is this
    where the water source is?

    The next thing you notice is an Elf sitting on the floor across the
    station in what seems to be a pile of colorful square cards.

    "Oh! Hello!" The Elf excitedly runs over to you. "How may I be of
    service?" You ask about water sources.

    "I'm not sure; I just operate the gondola lift. That does sound like
    something we'd have, though - this is Island Island, after all! I bet the
    gardener would know. He's on a different island, though - er, the small
    kind surrounded by water, not the floating kind. We really need to come
    up with a better naming scheme. Tell you what: if you can help me with
    something quick, I'll let you borrow my boat and you can go visit the
    gardener. I got all these scratchcards as a gift, but I can't figure out
    what I've won."

    The Elf leads you over to the pile of colorful cards. There, you discover
    dozens of scratchcards, all with their opaque covering already scratched
    off. Picking one up, it looks like each card has two lists of numbers
    separated by a vertical bar (|): a list of winning numbers and then a
    list of numbers you have. You organize the information into a table (your
    puzzle input).

    As far as the Elf has been able to figure out, you have to figure out
    which of the numbers you have appear in the list of winning numbers. The
    first match makes the card worth one point and each match after the first
    doubles the point value of that card.

    Take a seat in the large pile of colorful cards. How many points are they worth in total?
    """
    cards: list[Card] = parse_cards(filename)
    total_score = sum(card.evaluate() for card in cards)
    return total_score


def parse_cards(filename: str) -> list[Card]:
    """
    Parse the cards from the input file.

    :param filename: the name of the file to parse
    :return: a list of cards
    """
    # Use list comprehension
    with open(filename) as file:
        cards = [Card(line) for line in file.readlines()]

    return cards


if __name__ == '__main__':
    filename = 'input.txt'
    total_score = part_one(filename)
    print(total_score)