import unittest
from tictactoe.board import Board


class TestBoard(unittest.TestCase):
  def tests_boards_cells_are_empty(self):
    board = Board()

    for row in board.matrix:
      for cell in row:
        self.assertEqual(cell, ' ')

  def test_print_empty_board(self):
    board = Board()
    printed_board = board.__str__()

    self.assertEqual(printed_board, "  |   |  \n--+---+--\n  |   |  \n--+---+--\n  |   |  ")

  def test_player_X_starts(self):
    board = Board()

    self.assertEqual(board.player(), 'X')

  def test_player_O_goes_after_X(self):
    board = Board()
    board.play(0, 0)

    self.assertEqual(board.player(), 'O')

  def test_terminal_empty_board(self):
    board = Board()

    self.assertFalse(board.terminal())

  def test_terminal_full_board(self):
    board = Board()
    board.set_state([['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']])

    self.assertTrue(board.terminal())

  def test_terminal_X_wins(self):
    board = Board()
    board.set_state([['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']])

    self.assertTrue(board.terminal())

  def test_play_X(self):
    board = Board()
    board.play(0, 0)

    self.assertEqual(board.get_cell(0, 0), 'X')

  def test_play_O(self):
    board = Board()
    board.play(0, 0)
    board.play(0, 1)

    self.assertEqual(board.get_cell(0, 1), 'O')


# Run the tests
if __name__ == '__main__':
  unittest.main()
