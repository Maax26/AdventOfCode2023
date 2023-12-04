_DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def _get_first_digit(line):
    line = line.strip()
    for i, c in enumerate(line):
        if c.isdigit():
            return c
        for digit in _DIGITS.keys():
            if digit in line[i:i + len(digit)]:
                return _DIGITS[digit]


def _get_last_digit(line):
    line_reversed = line.strip()[::-1]
    for i, c in enumerate(line_reversed):
        if c.isdigit():
            return c
        for digit in _DIGITS.keys():
            if digit[::-1] in line_reversed[i:i + len(digit)]:
                return _DIGITS[digit]


def main():
    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    total_sum = 0
    for line in inputs:
        number_str = _get_first_digit(line)
        number_str += _get_last_digit(line)
        total_sum += int(number_str)

    print(total_sum)


if __name__ == "__main__":
    main()
