import sys


def main():
    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    seeds = inputs.readline().split()[1:]

    minimum_place = sys.maxsize
    for seed in seeds:
        inputs = open("test_input.txt")
        current_place = int(seed)  # Start on the seed location.
        check_minimum = False
        next_category = False
        current_category = ""
        for line in inputs:
            # if "location" in line:
            #     print(f"Current Location: {current_place}")
            #     check_minimum = True
            #     continue
            if not line[0].isdigit():
                if "map" in line:
                    current_category = line
                    next_category = False
                check_minimum = False
                continue
            if next_category:
                continue

            destination_range_start, source_range_start, range_length = [
                int(n) for n in line.split()
            ]

            # If the current line in the input is affecting the mapping of the current location.
            if source_range_start <= current_place < source_range_start + range_length:
                current_place = destination_range_start + (
                    current_place - source_range_start
                )
                next_category = True
            if "location" in current_category and current_place < minimum_place:
                minimum_place = current_place

    print(minimum_place)


if __name__ == "__main__":
    main()
