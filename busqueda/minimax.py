# Player constants
PLAYER_X = 'X'
PLAYER_O = 'O'

# Returns the current player
def player(state):
  count_x = sum(row.count(PLAYER_X) for row in state)
  count_o = sum(row.count(PLAYER_O) for row in state)
  return PLAYER_X if count_x == count_o else PLAYER_O

# Returns a list of possible actions in the current state
def actions(state):
  possible_actions = []
  for i in range(3):
    for j in range(3):
      if state[i][j] == ' ':
        possible_actions.append((i, j))
  return possible_actions

# Returns the new state after applying the given action
def result(state, action):
  new_state = [row[:] for row in state]
  new_state[action[0]][action[1]] = player(state)
  return new_state

# Returns True if the game is over, False otherwise
def terminal(state):
  # Check rows
  for row in state:
    if row[0] == row[1] == row[2] != ' ':
      return True

  # Check columns
  for j in range(3):
    if state[0][j] == state[1][j] == state[2][j] != ' ':
      return True

  # Check diagonals
  if state[0][0] == state[1][1] == state[2][2] != ' ':
    return True
  if state[0][2] == state[1][1] == state[2][0] != ' ':
    return True

  # Check if the board is full
  for row in state:
    if ' ' in row:
      return False
  return True

# Returns the utility value of the terminal state
def utility(state):
  # Check rows
  for row in state:
    if row[0] == row[1] == row[2] == PLAYER_X:
      return 1
    elif row[0] == row[1] == row[2] == PLAYER_O:
      return -1

  # Check columns
  for j in range(3):
    if state[0][j] == state[1][j] == state[2][j] == PLAYER_X:
      return 1
    elif state[0][j] == state[1][j] == state[2][j] == PLAYER_O:
      return -1

  # Check diagonals
  if state[0][0] == state[1][1] == state[2][2] == PLAYER_X:
    return 1
  elif state[0][0] == state[1][1] == state[2][2] == PLAYER_O:
    return -1
  if state[0][2] == state[1][1] == state[2][0] == PLAYER_X:
    return 1
  elif state[0][2] == state[1][1] == state[2][0] == PLAYER_O:
    return -1

  # If the game is a draw
  return 0

# Returns the minimax value of the current state
def minimax(state):
  def max_value(state):
    if terminal(state):
      return utility(state)
    v = float('-inf')
    for action in actions(state):
      v = max(v, min_value(result(state, action)))
    return v

  def min_value(state):
    if terminal(state):
      return utility(state)
    v = float('inf')
    for action in actions(state):
      v = min(v, max_value(result(state, action)))
    return v

  if player(state) == PLAYER_X:
    print("Player X")
    return max_value(state)
  else:
    print("Player O")
    return min_value(state)

if __name__ == "__main__":

    # board = [['X', ' ', ' '],
    #          [' ', 'O', ' '],
    #          ['X', 'O', ' ']]
    board = [['X', 'X', 'O'],
             ['X', 'O', ' '],
             ['X', 'O', ' ']]
    print(minimax(board))
