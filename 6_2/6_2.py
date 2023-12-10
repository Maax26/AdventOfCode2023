def main():
    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    times = inputs.readline().split()[1:]
    time = int("".join(times))
    distances = inputs.readline().split()[1:]
    distance = int("".join(distances))

    possible_wins = 0
    for time_pressed in range(time):
        travelled_distance = time_pressed * (time - time_pressed)
        if travelled_distance > distance:
            possible_wins += 1

    print(possible_wins)


if __name__ == "__main__":
    main()
