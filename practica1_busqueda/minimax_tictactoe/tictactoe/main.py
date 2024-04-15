from board import Board

if __name__ == '__main__':
    # state = [['X', 'O', ' '],[ ' ', 'X', ' '],[' ', ' ', 'O']]
    board = Board(size=4)
    print(board)
    print(board.player())
    print(board.actions())
    print(board.terminal())
    print(board.play(0, 2))
    print(board)

    # Implementar Minimax
