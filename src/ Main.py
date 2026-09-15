import random
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()
def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    for a, b, c in winning_combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False
def is_draw(board):
    return " " not in board
def minimax(board, is_maximizing):
    if check_winner(board, "X"):
        return 1
    if check_winner(board, "O"):
        return -1
    if is_draw(board):
        return 0
    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score
def minimax_move(board):
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move
def random_move(board):
    available_moves = []
    for i in range(9):
        if board[i] == " ":
            available_moves.append(i)
    return random.choice(available_moves)
def play_game():
    board = [" "] * 9
    print("================================")
    print("     MINIMAX vs RANDOM PLAYER")
    print("================================")
    print("Minimax Player : X")
    print("Random Player  : O")
    display_board(board)
    for turn in range(9):
        if turn % 2 == 0:
            move = minimax_move(board)
            board[move] = "X"
            print("Minimax Player chose position:", move + 1)
            display_board(board)
            if check_winner(board, "X"):
                print("Minimax Player (X) Wins!")
                return
        else:
            move = random_move(board)
            board[move] = "O"
            print("Random Player chose position:", move + 1)
            display_board(board)
            if check_winner(board, "O"):
                print("Random Player (O) Wins!")
                return
    print("The Game is a Draw!")
if __name__ == "__main__":
    play_game()
