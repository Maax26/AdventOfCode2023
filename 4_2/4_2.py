from collections import defaultdict


def main():
    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    card_instances = defaultdict(int)
    p1 = 0
    for i, card in enumerate(inputs):
        card_instances[i] += 1
        card_str, numbers_str = card.strip().split(":")
        winning_numbers_str, your_numbers_str = numbers_str.strip().split("|")
        winning_numbers = [w for w in winning_numbers_str.strip().split(" ") if w]
        your_numbers = [y for y in your_numbers_str.strip().split(" ") if y]

        your_winning_numbers = set(your_numbers).intersection(winning_numbers)

        if len(your_winning_numbers) > 0:
            p1 += 2**(len(your_winning_numbers)-1)
        for j in range(len(your_winning_numbers)):
            card_instances[i+1+j] += card_instances[i]

    print(p1)
    print(sum(card_instances.values()))


if __name__ == "__main__":
    main()