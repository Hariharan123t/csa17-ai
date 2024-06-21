# Initialize an empty 8x8 board
board = [[0 for _ in range(8)] for _ in range(8)]

# Function to print the board
def print_board():
    for row in board:
        print(" ".join(map(str, row)))
    print("\n")

# Function to check if a queen can be placed at a given position
def is_safe(row, col):
    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal
    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

# Function to solve the 8 queens problem using backtracking
def solve_queens(col):
    if col >= 8:
        print_board()
        return True
    
    for i in range(8):
        if is_safe(i, col):
            board[i][col] = 1
            solve_queens(col + 1)
            board[i][col] = 0

# Solve the 8 queens problem
solve_queens(0)
