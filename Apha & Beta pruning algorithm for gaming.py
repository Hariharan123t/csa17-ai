import math

def evaluate(board):
    for row in board:
        if all(cell == 'X' for cell in row):
            return 1
        elif all(cell == 'O' for cell in row):
            return -1
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 1
        elif all(board[row][col] == 'O' for row in range(3)):
            return -1
    if all(board[i][i] == 'X' for i in range(3)):
        return 1
    elif all(board[i][2-i] == 'X' for i in range(3)):
        return 1
    elif all(board[i][i] == 'O' for i in range(3)):
        return -1
    elif all(board[i][2-i] == 'O' for i in range(3)):
        return -1
    return 0

def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)
    if score != 0 or depth == 0:
        return score
    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth - 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth - 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def get_best_move(board):
    best_move = None
    best_eval = -math.inf
    alpha = -math.inf
    beta = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                eval = minimax(board, 4, False, alpha, beta)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        human_row = int(input("Enter row: "))
        human_col = int(input("Enter column: "))
        board[human_row][human_col] = 'O'
        print_board(board)
        if evaluate(board) == -1:
            print("You win!")
            break
        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            print("It's a tie!")
            break
        print("Computer is thinking...")
        computer_row, computer_col = get_best_move(board)
        board[computer_row][computer_col] = 'X'
        if evaluate(board) == 1:
            print_board(board)
            print("Computer wins!")
            break

main()
