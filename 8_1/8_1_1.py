def main():
    inputs = open("test_input.txt", encoding="utf-8")

    current_location = "AAA"
    goal_location = "ZZZ"

    instructions = list(inputs.readline().strip())

    for line in inputs:
        if " = " not in line:
            continue
        map_location, elements = line.strip().split(" = ")
        print(map_location, elements)


if __name__ == "__main__":
    main()