from src.minimax_vs_random 
import check_winner, is_draw
def test_x_winner():
    board = [
        "X", "X", "X",
        " ", "O", " ",
        " ", " ", "O"
    ]
    assert check_winner(board, "X") == True
def test_o_winner():
    board = [
        "O", "O", "O",
        " ", "X", " ",
        "X", " ", " "
    ]
    assert check_winner(board, "O") == True
def test_no_winner():
    board = [
        "X", "O", "X",
        "O", "X", "O",
        "O", "X", "O"
    ]
    assert check_winner(board, "X") == False
def test_draw():
    board = [
        "X", "O", "X",
        "O", "X", "O",
        "O", "X", "O"
    ]
    assert is_draw(board) == True
def test_not_draw():
    board = [
        "X", "O", " ",
        " ", "X", " ",
        " ", " ", "O"
    assert is_draw(board) == False
