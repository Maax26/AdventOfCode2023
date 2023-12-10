def main():
    # inputs = open("test_input.txt", encoding="utf-8")
    inputs = open("input.txt", encoding="utf-8")

    total_points = 0
    for card in inputs:
        numbers_str = card.strip().split(":")[1]
        winning_numbers_str, your_numbers_str = numbers_str.strip().split("|")
        winning_numbers = [w for w in winning_numbers_str.strip().split(" ") if w]
        your_numbers = [y for y in your_numbers_str.strip().split(" ") if y]

        your_winning_numbers = set(your_numbers).intersection(winning_numbers)
        total_points += int(2 ** (len(your_winning_numbers) - 1))

    print(total_points)


if __name__ == "__main__":
    main()
