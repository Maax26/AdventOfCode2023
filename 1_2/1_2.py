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


def get_first_digit(line):
    stripped_line = line.strip()
    for i, c in enumerate(stripped_line):
        if c.isdigit():
            return c
        for digit in _DIGITS.keys():
            if digit in stripped_line[i:i+len(digit)]:
                return _DIGITS[digit]


def get_last_digit(line):
    line_reversed = line.strip()[::-1]
    for i, c in enumerate(line_reversed):
        if c.isdigit():
            return c
        for digit in _DIGITS.keys():
            if digit[::-1] in line_reversed[i:i+len(digit)]:
                return _DIGITS[digit]


if __name__ == "__main__":
    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    total_sum = 0
    for input_line in inputs:
        number_str = get_first_digit(input_line)
        number_str += get_last_digit(input_line)
        total_sum += int(number_str)

    print(total_sum)