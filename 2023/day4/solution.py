import re
from collections import defaultdict


class Card:
    def __init__(self, line: str):
        """
        Parse a card from a line of text.

        :param line: the line of text to parse
        """
        card_id, line = line.strip().split(': ')
        self.card_number = int(re.search(r'(\d+)', card_id).group())

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

    @property
    def matches(self) -> list[int]:
        return [yn for yn in self.your_numbers if yn in self.winning_numbers]

    @property
    def points(self) -> int:
        num_matches: int = len(self.matches)
        return 2 ** (num_matches - 1) if num_matches else 0

    def get_copies(self) -> set[int]:
        num_matches: int = len(self.matches)
        start = self.card_number + 1
        end = start + num_matches
        return set(range(start, end))


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
    total_score = sum(card.points for card in cards)
    return total_score


def part_two(filename):
    """
    --- Part Two ---
    Just as you're about to report your findings to the Elf, one of you
    realizes that the rules have actually been printed on the back of every
    card this whole time.

    There's no such thing as "points". Instead, scratchcards only cause you
    to win more scratchcards equal to the number of winning numbers you have.

    Specifically, you win copies of the scratchcards below the winning card
    equal to the number of matches. So, if card 10 were to have 5 matching
    numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.

    Copies of scratchcards are scored like normal scratchcards and have the
    same card number as the card they copied. So, if you win a copy of card
    10 and it has 5 matching numbers, it would then win a copy of the same
    cards that the original card 10 won: cards 11, 12, 13, 14, and 15. This
    process repeats until none of the copies cause you to win any more cards.
    (Cards will never make you copy a card past the end of the table.)

    Process all of the original and copied scratchcards until no more
    scratchcards are won. Including the original set of scratchcards,
    how many total scratchcards do you end up with?
    """
    cards: list[Card] = parse_cards(filename)
    card_counts = {card.card_number: 1 for card in cards}
    for card in cards:
        copies = card.get_copies()
        for copy in copies:
            card_counts[copy] += card_counts[card.card_number]

    return sum(card_counts.values())


def parse_cards(filename: str) -> list[Card]:
    with open(filename) as file:
        cards = [Card(line) for line in file.readlines()]

    return cards


if __name__ == '__main__':
    filename = 'input.txt'
    total_score = part_one(filename)
    total_num_cards = part_two(filename)
    print(total_score)
    print(total_num_cards)