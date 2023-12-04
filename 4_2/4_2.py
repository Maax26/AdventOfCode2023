def main():
    inputs = open("test_input.txt")

    card_instances = [1]

    for card in inputs:
        card_str, numbers_str = card.strip().split(":")
        winning_numbers_str, your_numbers_str = numbers_str.strip().split("|")
        winning_numbers = [w for w in winning_numbers_str.strip().split(" ") if w]
        your_numbers = [y for y in your_numbers_str.strip().split(" ") if y]

        your_winning_numbers = set(your_numbers).intersection(winning_numbers)

        for i in range(len(your_winning_numbers)):
            card_instance = card_instances.get(str(i+1), 1)
            key_string = str(i+1)

            card_instances.update(=card_instance)

        # print(f"{card_str}: {your_winning_numbers}")

    print(card_instances)

if __name__ == "__main__":
    main()
