def _get_first_digit(line):
    for c in line:
        if c.isdigit():
            return c
    return ""


def main():
    # inputs = open("test_input.txt", encoding="utf-8")
    inputs = open("input.txt", encoding="utf-8")

    total_sum = 0
    for line in inputs:
        number_str = _get_first_digit(line)
        number_str += _get_first_digit(line[::-1])
        total_sum += int(number_str)

    print(total_sum)


if __name__ == "__main__":
    main()
