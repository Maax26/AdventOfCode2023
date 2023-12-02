if __name__ == "__main__":
    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    total_sum = 0
    for game in inputs:
        game = game.strip()
        game_str, all_sets = game.split(":")
        game_n = int(game_str.split(" ")[1])

        sets = all_sets.strip().split(";")
        max_colors = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for g_set in sets:
            for pull in g_set.split(","):
                pull = pull.strip()
                n_color, color = pull.split(" ")

                if int(n_color) > max_colors[color]:
                    max_colors[color] = int(n_color)
        power = max_colors["red"] * max_colors["green"] * max_colors["blue"]
        total_sum += power

    print(total_sum)
