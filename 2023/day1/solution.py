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


def part_one(filename):
    with open(filename) as file:
        sum_of_calibration_values = 0
        while line := file.readline().strip():
            calibration_value = find_first_and_last_digits(line)
            sum_of_calibration_values += calibration_value

    return sum_of_calibration_values


def part_two(filename):
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

