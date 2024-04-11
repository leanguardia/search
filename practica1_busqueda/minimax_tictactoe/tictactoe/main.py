from board import Board

if __name__ == '__main__':
    board = Board([['X', 'O', ' '],[ ' ', 'X', ' '],[' ', ' ', 'O']])
    print(board)
    print(board.player())
    print(board.actions())
    print(board.terminal())
    print(board.play(0, 2))
    print(board)

    # Implementar Minimax
