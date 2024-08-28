grid_ = [
        [5, 0, 4, 0, 6, 0, 0, 0, 0],
        [9, 0, 8, 0, 7, 0, 1, 0, 5],
        [0, 0, 0, 8, 0, 0, 0, 0, 9],
        [0, 1, 0, 0, 0, 3, 7, 9, 0],
        [0, 0, 9, 7, 0, 1, 8, 0, 0],
        [0, 8, 7, 4, 0, 0, 0, 2, 0],
        [6, 0, 0, 0, 0, 8, 0, 0, 0],
        [7, 0, 1, 0, 3, 0, 9, 0, 8],
        [0, 0, 0, 0, 5, 0, 6, 0, 2],
    ]


def display_grid(grid):
    for x in range(9):
        for y in range(9):
            print(grid[x][y], end=" ")
        print()


def check_valid(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for y in range(9):
        if grid[y][col] == num:
            return False

    c_row = row - row % 3
    c_col = col - col % 3


    for x in range(3):
        for y in range(3):
            if grid[c_row + x][c_col + y] == num:
                return False

    return True

def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return grid
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col+1)

    for i in range(1, 10):
        if check_valid(grid, row, col, i):
            grid[row][col] = i
            if solve(grid, row, col + 1):
                return True

        grid[col][row] = 0

    return False