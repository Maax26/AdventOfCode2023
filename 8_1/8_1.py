def main():
    # inputs = open("test_input.txt", encoding="utf-8")
    inputs = open("input.txt", encoding="utf-8")

    current_location = "AAA"
    goal_location = "ZZZ"

    instructions = list(inputs.readline().strip())
    current_instruction = 0

    n_steps = 0
    while current_location != goal_location:
        if current_instruction >= len(instructions):
            current_instruction = 0

        line = inputs.readline()
        if not line:
            # inputs = open("test_input.txt", encoding="utf-8")
            inputs = open("input.txt", encoding="utf-8")

        if " = " not in line:
            continue
        map_location, elements = line.strip().split(" = ")
        if map_location != current_location:
            continue

        elements = elements[1:-1].split(", ")

        if instructions[current_instruction] == "L":
            current_location = elements[0]
        if instructions[current_instruction] == "R":
            current_location = elements[1]

        current_instruction += 1
        n_steps += 1

    print(n_steps)


if __name__ == "__main__":
    main()
