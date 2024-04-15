class Board():
  def __init__(self, size=3, state=None):
    self.size = size
    self.matrix = state or [[' ' for _ in range(self.size)] for _ in range(self.size)]
    self.max_player = 'X'
    self.min_player = 'O'

  def __str__(self):
    row_separator = '\n' + '--' + '+---' * (self.size - 2) + '+--\n'
    return (row_separator.join([' | '.join(row) for row in self.matrix])) + '\n'

  def player(self):
    x_count = sum(row.count('X') for row in self.matrix)
    o_count = sum(row.count('O') for row in self.matrix)

    return self.max_player if x_count == o_count else self.min_player
  
  def terminal(self):
    for row in self.matrix:
      if row[0] == row[1] == row[2] != ' ':
        return True

    for j in range(self.size):
      if self.matrix[0][j] == self.matrix[1][j] == self.matrix[2][j] != ' ':
        return True

    if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] != ' ':
      return True
    if self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] != ' ':
      return True

    for row in self.matrix:
      if ' ' in row:
        return False
    return True
  
  def play(self, action):
    self.matrix[action[0]][action[1]] = self.player() 
    return self

  def actions(self):
    possible_actions = []
    for i in range(self.size):
      for j in range(self.size):
        if self.matrix[i][j] == ' ':
          possible_actions.append((i, j))
    return possible_actions
  
  def utility(self):
    for row in self.matrix:     # Rows
      are_equal = True
      for j in range(self.size-1):
        if row[j] != row[j+1]:
          are_equal = False
          break
      if are_equal:
        if row[0] == 'X':
          return 1
        elif row[0] == 'O':
          return -1

    for j in range(self.size):   # Columns
      if self.matrix[0][j] == self.matrix[1][j] == self.matrix[2][j] == 'X':
        return 1
      elif self.matrix[0][j] == self.matrix[1][j] == self.matrix[2][j] == 'O':
        return -1

    if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == 'X':
      return 1
    elif self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == 'O':
      return -1
    if self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == 'X':
      return 1
    elif self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == 'O':
      return -1

    return 0

  def get_cell(self, i, j):
    return self.matrix[i][j]

  def set_state(self, state):
    self.matrix = state

  def get_state(self):
    return self.matrix
