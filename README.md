# Sudoku Solver

This is a Python program that solves Sudoku puzzles using a recursive backtracking algorithm. It includes functions to generate a random Sudoku board and solve an existing board.

## Code Explanation
The code consists of several functions:

### `printBoard()`
This function prints the current state of the Sudoku board. It iterates over each cell and displays its value.

### `possible(x, y, n)`
This function checks if it is possible to place a number `n` in the cell at coordinates `(x, y)` on the Sudoku board. It verifies if the number already exists in the same row, column, or block, returning `False` if it violates the rules of Sudoku. Otherwise, it returns `True`.

### `generate_board()`
This function generates a random Sudoku board by randomly placing numbers in 25 cells. It uses the `possible()` function to ensure the numbers are valid. Once the board is generated, it calls `printBoard()` to display the result.

### `solve()`
This function solves the Sudoku puzzle using a recursive backtracking algorithm. It starts by finding an empty cell (marked as `0`) and tries every possible number from 1 to 9 in that cell using the `possible()` function. If a valid number is found, it places it in the cell and recursively calls `solve()` to move on to the next cell. If the solver reaches a point where it cannot find a valid number for a cell, it backtracks and tries a different number in the previous cell. This continues until a solution is found. Finally, it calls `printBoard()` to display the solved Sudoku board.

## Usage
1. Make sure you have Python installed on your system.
2. Copy and save the code into a Python file (e.g., `sudoku_solver.py`).
3. Run the Python file using the command: `python sudoku_solver.py`.

## Running the Program
1. The initial state of the empty Sudoku board is printed by calling `printBoard()`.
2. A randomly generated Sudoku board is created by calling `generate_board()`. This board serves as the starting point for the solver.
3. The `solve()` function is called to solve the Sudoku puzzle. If a solution is found, the solved board is displayed using `printBoard()`.
4. The program exits.
