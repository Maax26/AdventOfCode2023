def make_map(text):
    ret_map = []
    for i, r in enumerate(text):
        r = r.strip()
        ret_map.append([])
        for j, c in enumerate(r):
            ret_map[i].append(c)

    return ret_map

def has_part_neighbor(grid_map, row_idx, col_idx):
    num_rows = len(grid_map)
    num_cols = len(grid_map[0])

    for i in range(row_idx - 1, row_idx + 2):
        for j in range(col_idx - 1, col_idx + 2):
            if 0 <= i < num_rows and 0 <= j < num_cols and (i != row_idx or j != col_idx):
                if not grid_map[i][j].isdigit() and grid_map[i][j] != ".":
                    return True
    return False


if __name__ == "__main__":
    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    grid_map = make_map(inputs)

    total_sum = 0
    for i in range(len(grid_map)):
        current_number_str = ""
        is_part = False
        for j in range(len(grid_map)):
            if grid_map[i][j].isdigit():
                current_number_str += grid_map[i][j]
                if not is_part:
                    is_part = has_part_neighbor(grid_map, i, j)
            else:
                if is_part:
                    total_sum += int(current_number_str)
                current_number_str = ""
                is_part = False
        if current_number_str and is_part:
            total_sum += int(current_number_str)

    print(total_sum)