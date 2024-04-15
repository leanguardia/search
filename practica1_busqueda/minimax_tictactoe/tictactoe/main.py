from board import Board

def minimax(board):
    if board.terminal():
        return board.utility()

    if board.player() == board.max_player:
        print("Max plays")
        value = float('-inf')
        for action in board.actions():
            value = max(value, minimax(board.play(action)))
        return value
    else:
        value = float('inf')
        print("Min plays")
        for action in board.actions():
            value = min(value, minimax(board.play(action)))
        return value

if __name__ == '__main__':
    # state = [['X', 'O', ' '],[ ' ', 'X', ' '],[' ', ' ', 'O']]
    board = Board(size=3)
    print(board)
    # print(board.player())
    # print(board.actions())
    # print(board.terminal())
    # print(board.play(0, 2))

    # Implementar Minimax
    minimax_value = minimax(board)
    print(minimax_value)
