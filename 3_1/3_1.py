def _make_schematic(inputs):
    schematic = []
    for i, row in enumerate(inputs):
        row = row.strip()
        schematic.append([])
        for col in row:
            schematic[i].append(col)
    return schematic


def _has_part_neighbor(schematic, row, col):
    n_rows = len(schematic)
    n_cols = len(schematic[0])

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < n_rows and 0 <= j < n_cols and (i != row or j != col):
                if not schematic[i][j].isdigit() and schematic[i][j] != ".":
                    return True
    return False


def main():
    # inputs = open("test_input.txt", encoding="utf-8")
    inputs = open("input.txt", encoding="utf-8")

    schematic = _make_schematic(inputs)

    total_sum = 0
    for i, row in enumerate(schematic):
        current_number_str = ""
        is_part = False
        for j, col in enumerate(row):
            if col.isdigit():
                current_number_str += col
                if not is_part:
                    is_part = _has_part_neighbor(schematic, i, j)
            else:
                if is_part:
                    total_sum += int(current_number_str)
                current_number_str = ""
                is_part = False
        if current_number_str and is_part:
            total_sum += int(current_number_str)

    print(total_sum)


if __name__ == "__main__":
    main()
