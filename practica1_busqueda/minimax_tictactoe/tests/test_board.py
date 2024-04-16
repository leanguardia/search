import unittest
from tictactoe.board import Board


class TestBoard(unittest.TestCase):
    def tests_boards_cells_are_empty(self):
        board = Board()

        for row in board.to_matrix():
            for cell in row:
                self.assertEqual(cell, ' ')

    def tests_three_is_the_default_size(self):
        board = Board()

        self.assertEqual(board.get_size(), 3)

    def tests_board_can_be_created_with_a_custom_size(self):
        board = Board(size=4)

        self.assertEqual(board.get_size(), 4)

    def test_print_empty_3x3_board(self):
        board = Board()
        printed_board = board.__str__()

        self.assertEqual(printed_board, "  |   |  \n--+---+--\n  |   |  \n--+---+--\n  |   |  \n")

    def test_print_empty_4x4_board(self):
        board = Board(size=4)
        printed_board = board.__str__()

        self.assertEqual(printed_board, "  |   |   |  \n--+---+---+--\n  |   |   |  \n--+---+---+--\n  |   |   |  \n--+---+---+--\n  |   |   |  \n")

    def test_player_X_starts(self):
        board = Board()

        self.assertEqual(board.player(), 'X')

    def test_play_X(self):
        board = Board()
        board.play((0, 0))

        self.assertEqual(board.get_cell(0, 0), 'X')

    def test_play_O(self):
        board = Board()
        board.play((0, 0))
        board.play((0, 1))

        self.assertEqual(board.get_cell(0, 1), 'O')


    # Describe #player()
    def test_player_O_goes_after_X(self):
        board = Board()
        board.play((0, 0))

        self.assertEqual(board.player(), 'O')

    def test_players_alternate_turns(self):
        board = Board()
        self.assertEqual(board.player(), 'X')
        board.play((0, 0))
        self.assertEqual(board.player(), 'O')
        board.play((1, 1))
        self.assertEqual(board.player(), 'X')
        board.play((2, 2))
        self.assertEqual(board.player(), 'O')
        board.play((0, 1))
        self.assertEqual(board.player(), 'X')


    # Describe #terminal()
    def test_terminal_empty_board(self):
        board = Board()

        self.assertFalse(board.terminal())

    def test_terminal_full_board(self):
        board = Board()
        board.set_state([['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']])

        self.assertTrue(board.terminal())

    def test_terminal_X_wins(self):
        board = Board()
        board.set_state([['X', 'O', 'X'], ['O', 'X', 'O'], ['X', ' ', ' ']])

        self.assertTrue(board.terminal())

    def test_terminal_partial_board(self):
        board = Board()
        board.set_state([['X', 'O', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']])

        self.assertFalse(board.terminal())


    # Describe #utility()
    def test_utility_X_wins_diagonal(self):
        board = Board()
        board.set_state([['X', 'O', ' '], [' ', 'X', ' '], [' ', 'O', 'X']])

        self.assertEqual(board.utility(), 1)

    def test_utility_X_wins_column(self):
        board = Board()
        board.set_state([['X', 'O', ' '], ['X', 'O', ' '], ['X', ' ', ' ']])

        self.assertEqual(board.utility(), 1)

    def test_utility_O_wins_row(self):
        board = Board()
        board.set_state([['O', 'O', 'O'], ['X', 'X', ' '], ['X', ' ', ' ']])

        self.assertEqual(board.utility(), -1)

    def test_utility_O_wins_column(self):
        board = Board()
        board.set_state([['X', 'O', ' '], [' ', 'O', ' '], ['X', 'O', 'X']])

        self.assertEqual(board.utility(), -1)

    def test_utility_draw(self):
        board = Board()
        board.set_state([['X', 'O', 'X'], ['O', 'O', 'X'], ['X', 'X', 'O']])

        self.assertEqual(board.utility(), 0)


# Run the tests
if __name__ == '__main__':
    unittest.main()
