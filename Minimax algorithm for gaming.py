import math

# Constants
X = 'X'
O = 'O'
EMPTY = ' '

# Function to print the Tic Tac Toe board
def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

# Function to check if the board is full
def board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to evaluate the current state of the board
def evaluate(board):
    if check_win(board, X):
        return 1
    elif check_win(board, O):
        return -1
    else:
        return 0

# Minimax algorithm function
def minimax(board, depth, is_maximizing):
    if check_win(board, X):
        return 1
    elif check_win(board, O):
        return -1
    elif board_full(board):
        return 0
    
    if is_maximizing:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = X
                    eval = minimax(board, depth+1, False)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = O
                    eval = minimax(board, depth+1, True)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move using Minimax algorithm
def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = X
                eval = minimax(board, 0, False)
                board[row][col] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

# Function to play the game
def play_game():
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    current_player = X
    
    while True:
        print_board(board)
        
        if current_player == X:
            row, col = find_best_move(board)
            print(f"Player X moves to row {row} col {col}")
            board[row][col] = X
        else:
            row, col = map(int, input(f"Player O, enter your move (row [0-2] col [0-2]): ").split())
            if board[row][col] != EMPTY:
                print("Invalid move. Try again.")
                continue
            board[row][col] = O
        
        if check_win(board, X):
            print_board(board)
            print("Player X wins!")
            break
        elif check_win(board, O):
            print_board(board)
            print("Player O wins!")
            break
        elif board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = O if current_player == X else X

# Start the game
if __name__ == "__main__":
    play_game()
