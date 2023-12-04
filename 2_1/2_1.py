_COLORS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def main():
    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    total_sum = 0
    for game in inputs:
        game = game.strip()
        game_str, all_sets = game.split(":")
        game_n = int(game_str.split(" ")[1])

        sets = all_sets.strip().split(";")
        all_pulls_legal = True
        for g_set in sets:
            for pull in g_set.split(","):
                pull = pull.strip()
                n_color, color = pull.split(" ")
                if int(n_color) > _COLORS[color]:
                    all_pulls_legal = False
        if all_pulls_legal:
            total_sum += game_n

    print(total_sum)


if __name__ == "__main__":
    main()
