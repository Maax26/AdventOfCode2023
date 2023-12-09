def main():
    next_tile = "AAA"
    current_tile = ""
    mapping = ""
    while next_tile != "ZZZ":
        inputs = open("test_input.txt")
        instructions = [c for c in inputs.readline().strip()]
        inputs.readline()
        for instruction in instructions:
            while next_tile != current_tile:
                if inputs.
                current_tile, mapping = inputs.readline().split(" = (")

            left, right = mapping.strip()[:-1].split(", ")
            if instruction == "L":
                next_tile = left
            if instruction == "R":
                next_tile = right
            print(left, right)


if __name__ == "__main__":
    main()
