DIGITS = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def find_first_digit_occurrence(
    line: str, numeric_only: bool = True, reversed_: bool = False
):
    line_ = reversed(line) if reversed_ else line
    word = ''
    for char in line_:
        if char.isnumeric():
            return char
        elif not numeric_only:
            word += char
            word_ = word[::-1] if reversed_ else word
            for digit_str, digit in DIGITS.items():
                if digit_str in word_:
                    return digit

    return


def find_first_and_last_digits(line: str) -> int:
    first = find_first_digit_occurrence(line)
    last = find_first_digit_occurrence(line, reversed_=True)
    return int(f'{first}{last}')


def find_first_and_last_digits_including_text(line: str) -> int:
    first = find_first_digit_occurrence(line, numeric_only=False)
    last = find_first_digit_occurrence(line, numeric_only=False, reversed_=True)
    return int(f'{first}{last}')


def part_one(filename: str) -> int:
    """
    --- Day 1: Trebuchet?! ---

    You try to ask why they can't just use a weather machine ("not powerful
    enough") and where they're even sending you ("the sky") and why your map
    looks mostly blank ("you sure ask a lot of questions") and hang on did
    you  just say the sky ("of course, where do you think snow comes from")
    when you realize that the Elves are already loading you into a trebuchet
    ("please hold still, we need to strap you in").

    As they're making the final adjustments, they discover that their
    calibration document (your puzzle input) has been amended by a very
    young Elf who was apparently just excited to show off her art skills.
    Consequently, the Elves are having trouble reading the values on the document.

    The newly-improved calibration document consists of lines of text; each
    line originally contained a specific calibration value that the Elves
    now need to recover. On each line, the calibration value can be found by
    combining the first digit and the last digit (in that order) to form a
    single two-digit number.


    Consider your entire calibration document. What is the sum of all of the calibration values?

    Your puzzle answer was 55712.
    """
    with open(filename) as file:
        sum_of_calibration_values = 0
        while line := file.readline().strip():
            calibration_value = find_first_and_last_digits(line)
            sum_of_calibration_values += calibration_value

    return sum_of_calibration_values


def part_two(filename: str) -> int:
    """
    our calculation isn't quite right. It looks like some of the digits are
    actually spelled out with letters: one, two, three, four, five, six,
    seven, eight, and nine also count as valid "digits".

    Equipped with this new information, you now need to find the real first
    and last digit on each line.

    What is the sum of all calibration values?
    """
    with open(filename) as file:
        sum_of_calibration_values = 0
        while line := file.readline().strip():
            calibration_value = find_first_and_last_digits_including_text(line)
            sum_of_calibration_values += calibration_value

    return sum_of_calibration_values


if __name__ == '__main__':
    filename = 'input.txt'
    sum_of_calibration_values = part_one(filename)
    sum_of_calibration_values_p2 = part_two(filename)
    print(sum_of_calibration_values)
    print(sum_of_calibration_values_p2)
