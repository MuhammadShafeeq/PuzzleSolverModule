import tkinter as tk

root = tk.Tk()

# Create the puzzle
puzzle = tk.Frame(root, bg='white')
puzzle.pack()

# Add the 3 * 3 big blocks
blocks = [[None] * 3] * 3
for i in range(3):
    for j in range(3):
        blocks[i][j] = tk.Frame(puzzle, bd=1, highlightbackground='light blue',
                                highlightcolor='light blue', highlightthickness=1)
        blocks[i][j].grid(row=i, column=j, sticky='nsew')

# Add the 9 * 9 cells
btn_cells = [[None] * 9] * 9
for i in range(9):
    for j in range(9):
        # Add cell to the block
        # Add a frame so that the cell can form a square
        frm_cell = tk.Frame(blocks[i // 3][j // 3])
        frm_cell.grid(row=(i % 3), column=(j % 3), sticky='nsew')
        frm_cell.rowconfigure(0, minsize=50, weight=1)
        frm_cell.columnconfigure(0, minsize=50, weight=1)
        var = tk.StringVar()
        btn_cells[i][j] = tk.Button(frm_cell, relief='ridge', bg='white', textvariable=var)
        btn_cells[i][j].grid(sticky='nsew')

        # Show the index for reference
        var.set(str((i, j)))

root.mainloop()