def _make_schematic(inputs):
    schematic = []
    for i, row in enumerate(inputs):
        row = row.strip()
        schematic.append([])
        for col in row:
            schematic[i].append(col)
    return schematic


def _find_gear_neighbor(schematic, row, col):
    n_rows = len(schematic)
    n_cols = len(schematic[0])

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < n_rows and 0 <= j < n_cols and (i != row or j != col):
                if schematic[i][j] == "*":
                    return f"{i}{j}"
    return ""


def main():  # pylint: disable=too-many-branches
    # inputs = open("test_input.txt", encoding="utf-8")
    inputs = open("input.txt", encoding="utf-8")

    schematic = _make_schematic(inputs)

    gear_neighbors = {}

    total_sum = 0
    for i, row in enumerate(schematic):
        current_number_str = ""
        gear_neighbor = ""
        for j, col in enumerate(row):
            if col.isdigit():
                current_number_str += col
                if not gear_neighbor:
                    gear_neighbor = _find_gear_neighbor(schematic, i, j)
            else:
                if gear_neighbor:
                    if gear_neighbors.get(gear_neighbor, 0):
                        gear_neighbors[gear_neighbor].append(int(current_number_str))
                    else:
                        gear_neighbors[gear_neighbor] = [int(current_number_str)]
                current_number_str = ""
                gear_neighbor = ""
        if current_number_str and gear_neighbor:
            if gear_neighbors.get(gear_neighbor, 0):
                gear_neighbors[gear_neighbor].append(int(current_number_str))
            else:
                gear_neighbors[gear_neighbor] = [int(current_number_str)]

    for values in gear_neighbors.values():
        if len(values) == 2:
            total_sum += int(values[0]) * int(values[1])

    print(total_sum)


if __name__ == "__main__":
    main()
