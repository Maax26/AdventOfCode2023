def main():
    # inputs = open("test_input.txt", encoding="utf-8")
    inputs = open("input.txt", encoding="utf-8")

    times_str = inputs.readline().split()[1:]
    times = [int(i) for i in times_str]
    distance_str = inputs.readline().split()[1:]
    distance = [int(i) for i in distance_str]

    table = list(zip(times, distance))

    margin_of_errors = 0
    for time, distance in table:
        wins_per_round = 0
        for time_pressed in range(time):
            travelled_distance = time_pressed * (time - time_pressed)
            if travelled_distance > distance:
                wins_per_round += 1
        if not margin_of_errors:
            margin_of_errors = wins_per_round
        else:
            margin_of_errors *= wins_per_round

    print(margin_of_errors)


if __name__ == "__main__":
    main()
