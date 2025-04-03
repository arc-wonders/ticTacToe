import math

def is_winner(board, player):
    """Checks if the given player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    """Checks if the board is full."""
    return all(cell != "_" for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha, beta):
    """Minimax algorithm with Alpha-Beta Pruning."""
    if is_winner(board, "O"):  # AI wins
        return 10 - depth
    if is_winner(board, "X"):  # Player wins
        return depth - 10
    if is_full(board):  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = "_"
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = "_"
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def get_best_move(board):
    """Finds the best possible move using Minimax."""
    best_score = -math.inf
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "O"
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = "_"
                
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    
    return best_move
