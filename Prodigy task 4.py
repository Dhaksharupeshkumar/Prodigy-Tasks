def solve_sudoku(board):
  """
  Solves a Sudoku puzzle using backtracking.

  Args:
      board: A 2D list representing the Sudoku puzzle grid.

  Returns:
      True if the puzzle is solved, False otherwise.
  """
  find = find_empty(board)
  if not find:
    return True
  row, col = find

  for i in range(1, 10):
    if is_valid(board, i, row, col):
      board[row][col] = i

      if solve_sudoku(board):
        return True

      board[row][col] = 0

  return False

def find_empty(board):
  """
  Finds an empty cell in the Sudoku grid.

  Args:
      board: A 2D list representing the Sudoku puzzle grid.

  Returns:
      A tuple (row, col) of the empty cell's coordinates, or None if all cells are filled.
  """
  for row in range(len(board)):
    for col in range(len(board[0])):
      if board[row][col] == 0:
        return row, col
  return None

def is_valid(board, num, row, col):
  """
  Checks if a number can be placed in a cell without violating Sudoku rules.

  Args:
      board: A 2D list representing the Sudoku puzzle grid.
      num: The number to be placed.
      row: The row index of the cell.
      col: The column index of the cell.

  Returns:
      True if the number can be placed, False otherwise.
  """
  # Check row
  for i in range(len(board[0])):
    if board[row][i] == num and col != i:
      return False

  # Check column
  for i in range(len(board)):
    if board[i][col] == num and row != i:
      return False

  # Check subgrid
  start_row = row - row % 3
  start_col = col - col % 3
  for i in range(3):
    for j in range(3):
      if board[start_row + i][start_col + j] == num and (row, col) != (start_row + i, start_col + j):
        return False

  return True

def print_board(board):
  """
  Prints the Sudoku board in a formatted way.
  """
  for i in range(len(board)):
    for j in range(len(board[0])):
      print(board[i][j], end=" ")
    print()

# Example usage
board = [
  [7, 8, 0, 4, 0, 0, 1, 2, 0],
  [6, 0, 0, 0, 7, 5, 0, 0, 9],
  [0, 0, 0, 6, 0, 1, 0, 7, 8],
  [0, 0, 7, 0, 4, 0, 2, 6, 0],
  [0, 5, 0, 0, 6, 0, 0, 1, 0],
  [0, 0, 3, 0, 1, 0, 7, 0, 0],
  [0, 3, 0, 1, 0, 0, 0, 0, 6],
  [9, 0, 0, 0, 2, 4, 0, 0, 3],
  [0, 0, 5, 0, 0, 0, 0, 8, 1]
]


print("Solved Sudoku:")
print_board(board)
