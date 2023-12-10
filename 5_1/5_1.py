from collections import defaultdict


def main():
    inputs = open("test_input.txt")

    # Keeping track of all mapping changes while going through the input
    mapping = {
        "soil": [*range(100)],
        "fertilizer": [*range(100)],
        "water": [*range(100)],
        "light": [*range(100)],
        "temperature": [*range(100)],
        "humidity": [*range(100)],
        "location": [*range(100)],
    }

    seeds = inputs.readline().split()[1:]

    current_category = ""
    for line in inputs:
        # If the line is empty
        if not line.strip():
            continue
        # Store the current category we are on.
        if "map" in line:
            current_category = line.split("-to-")[1].split("map")[0].strip()
            continue

        destination_range_start, source_range_start, range_length = line.split()
        for i in range(int(range_length)):
            # Updates the current categories array with the new value.
            mapping[current_category][int(source_range_start) + i] = (
                int(destination_range_start) + i
            )

    minimum_location_number = 100
    # Now that all mappings has been updated, go through all seeds.
    for seed in seeds:
        next_destination = int(seed)
        # Traverse through all the different categories and keep track of the next destination based on
        # the previous one.
        for category in mapping.keys():
            next_destination = mapping[category][next_destination]

        # Keep track of the lowest location number we find.
        if next_destination < minimum_location_number:
            minimum_location_number = next_destination

    print(minimum_location_number)


if __name__ == "__main__":
    main()
