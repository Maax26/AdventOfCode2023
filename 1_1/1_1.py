def get_first_digit(line):
    for c in line:
        if c.isdigit():
            return c


if __name__ == "__main__":
    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    total_sum = 0
    for input_line in inputs:
        number_str = get_first_digit(input_line)
        number_str += get_first_digit(input_line[::-1])
        total_sum += int(number_str)

    print(total_sum)
