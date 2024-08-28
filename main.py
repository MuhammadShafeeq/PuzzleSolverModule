# from SudokuSolver import SudokuSolver
#
# grid = [[5, 0, 4, 0, 6, 0, 0, 0, 0],
#         [9, 0, 8, 0, 7, 0, 1, 0, 5],
#         [0, 0, 0, 8, 0, 0, 0, 0, 9],
#         [0, 1, 0, 0, 0, 3, 7, 9, 0],
#         [0, 0, 9, 7, 0, 1, 8, 0, 0],
#         [0, 8, 7, 4, 0, 0, 0, 2, 0],
#         [6, 0, 0, 0, 0, 8, 0, 0, 0],
#         [7, 0, 1, 0, 3, 0, 9, 0, 8],
#         [0, 0, 0, 0, 5, 0, 6, 0, 2],
#         ]
#
# puz = SudokuSolver(grid=grid)
#
# puz.solve(0, 0)
#
# print()
# print("Solution")
# print()
# for i in range(9):
#     for j in range(9):
#         print(grid[i][j], end=" ")
#     print()


"""Soduku above"""

# CORRECT is a dictonary format {POSITION: CHAR}
# Its pythonic numerical (0..4)

# Misplaced is also dictionary with format {CHAR: [POS1, POS2, ...]}
# This is non pythonic (1..5)
#
# from WordleSolver import WordleSolver
#
# puz = WordleSolver()
# puz.set_words()
#
# correct = {0: "a", 4: "e"}
# misplaced = {"p": [1, 4]}
# incorrect = list("zxcbnmv")
#
# puz.set_correct(correct)
# puz.set_incorrect(incorrect)
# puz.set_misplaced(misplaced)
#
# puz.ch_letters()
# puz.ch_correct()
# puz.ch_misplaced()
#
# puz.set_solution()
# print(puz.get_solution())

"""Wordle Solver Usage"""

