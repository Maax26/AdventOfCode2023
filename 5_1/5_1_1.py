import sys


def main():
    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    seeds = inputs.readline().split()[1:]

    minimum_place = sys.maxsize
    for seed in seeds:
        inputs = open("input.txt")
        current_place = int(seed)  # Start on the seed location.
        for line in inputs:
            if not line[0].isdigit():
                continue

            destination_range_start, source_range_start, range_length = [int(n) for n in line.split()]

            # If the current line in the input is affecting the mapping of the current location.
            if source_range_start < current_place < source_range_start + range_length:
                current_place = destination_range_start + (current_place - source_range_start)
                if current_place < minimum_place:
                    minimum_place = current_place

    print(minimum_place)


if __name__ == "__main__":
    main()