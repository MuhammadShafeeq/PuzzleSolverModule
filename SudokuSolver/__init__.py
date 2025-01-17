NAME = "SudokuSolver"
VERSION = "0.0.1"


class SudokuSolver(object):
    def __init__(self, grid=None):
        self.grid = grid

    def set_grid(self, r1c1=0, r1c2=0, r1c3=0, r1c4=0, r1c5=0, r1c6=0, r1c7=0, r1c8=0, r1c9=0,
                 r2c1=0, r2c2=0, r2c3=0, r2c4=0, r2c5=0, r2c6=0, r2c7=0, r2c8=0, r2c9=0,
                 r3c1=0, r3c2=0, r3c3=0, r3c4=0, r3c5=0, r3c6=0, r3c7=0, r3c8=0, r3c9=0,
                 r4c1=0, r4c2=0, r4c3=0, r4c4=0, r4c5=0, r4c6=0, r4c7=0, r4c8=0, r4c9=0,
                 r5c1=0, r5c2=0, r5c3=0, r5c4=0, r5c5=0, r5c6=0, r5c7=0, r5c8=0, r5c9=0,
                 r6c1=0, r6c2=0, r6c3=0, r6c4=0, r6c5=0, r6c6=0, r6c7=0, r6c8=0, r6c9=0,
                 r7c1=0, r7c2=0, r7c3=0, r7c4=0, r7c5=0, r7c6=0, r7c7=0, r7c8=0, r7c9=0,
                 r8c1=0, r8c2=0, r8c3=0, r8c4=0, r8c5=0, r8c6=0, r8c7=0, r8c8=0, r8c9=0,
                 r9c1=0, r9c2=0, r9c3=0, r9c4=0, r9c5=0, r9c6=0, r9c7=0, r9c8=0, r9c9=0):

        self.grid = [[r1c1, r1c2, r1c3, r1c4, r1c5, r1c6, r1c7, r1c8, r1c9],
                     [r2c1, r2c2, r2c3, r2c4, r2c5, r2c6, r2c7, r2c8, r2c9],
                     [r3c1, r3c2, r3c3, r3c4, r3c5, r3c6, r3c7, r3c8, r3c9],
                     [r4c1, r4c2, r4c3, r4c4, r4c5, r4c6, r4c7, r4c8, r4c9],
                     [r5c1, r5c2, r5c3, r5c4, r5c5, r5c6, r5c7, r5c8, r5c9],
                     [r6c1, r6c2, r6c3, r6c4, r6c5, r6c6, r6c7, r6c8, r6c9],
                     [r7c1, r7c2, r7c3, r7c4, r7c5, r7c6, r7c7, r7c8, r7c9],
                     [r8c1, r8c2, r8c3, r8c4, r8c5, r8c6, r8c7, r8c8, r8c9],
                     [r9c1, r9c2, r9c3, r9c4, r9c5, r9c6, r9c7, r9c8, r9c9]
                     ]
        return self.grid

    def ch_valid(self, row, col, num):
        for x in range(9):
            if self.grid[row][x] == num:
                return False

        for x in range(9):
            if self.grid[x][col] == num:
                return False

        border_row = row - row % 3
        border_col = col - col % 3

        for x in range(3):
            for y in range(3):
                if self.grid[border_row + x][border_col + y] == num:
                    return False

        return True

    def solve(self, row, col):

        if col == 9:
            if row == 8:
                return True
            row += 1
            col = 0

        if self.grid[row][col] > 0:
            return self.solve( row=row, col=(col + 1))

        for i in range(1, 10):
            if self.ch_valid(row, col, num=i):
                self.grid[row][col] = i

                if self.solve(row=row, col=col + 1):
                    return True

            self.grid[row][col] = 0
        return False