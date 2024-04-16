from board import Board

def minimax(board):
    def max_value(board):
        if board.terminal():
            print(board, board.utility())

            return board.utility()
        v = float('-inf')
        for action in board.actions():
            v = max(v, min_value(board.play(action)))
        return v

    def min_value(board):
        if board.terminal():
            print(board, board.utility())

            return board.utility()
        v = float('inf')
        for action in board.actions():
            v = min(v, max_value(board.play(action)))
        return v

    if board.player() == board.max_player:
        return max_value(board)
    else:
        return min_value(board)

if __name__ == '__main__':
    state = [['X', 'O', 'X'],[ 'X', 'O', ' '],[' ', ' ', ' ']]
    board = Board(size=3, state=state)
    # print(board)

    minimax_value = minimax(board)
    print(minimax_value)

    # Checar estados terminales de ganar y tablero está incompleto
