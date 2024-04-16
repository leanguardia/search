import copy

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
        # Checks win on row
        for row in self.matrix:
            for j in range(self.size-1):
                if row[j] != row[j+1]:
                    break

        # Check win on column
        for j in range(self.size):
            for i in range(self.size-1):
                if self.matrix[i][j] != self.matrix[i+1][j]:
                    break

        # Check win on diagonals
        for i in range(self.size-1):
            if self.matrix[i][i] == ' ' or self.matrix[i][i] != self.matrix[i+1][i+1]:
                break
            if i == self.size - 2:
                return True
        for i in range(self.size):
            if self.matrix[i][self.size-1-i] == ' ' or self.matrix[i][self.size-1-i] != self.matrix[i+1][self.size-2-i]:
                break
            if i == self.size - 2:
                return True

        for row in self.matrix:
            if ' ' in row:
                return False
        return True

    def play(self, action):
        new_board = copy.deepcopy(self)
        new_board.matrix[action[0]][action[1]] = self.player()
        return new_board

    def actions(self):
        possible_actions = []
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] == ' ':
                    possible_actions.append((i, j))
        return possible_actions
    
    def utility(self):
        for row in self.matrix:          # Rows
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

        for j in range(self.size):          # Columns
            are_equal = True
            for i in range(self.size-1):
                if self.matrix[i][j] != self.matrix[i+1][j]:
                    are_equal = False
                    break
            if are_equal:
                if self.matrix[0][j] == 'X':
                    return 1
                elif self.matrix[0][j] == 'O':
                    return -1

        for i in range(self.size-1):          # Diagonals
            if self.matrix[i][i] != self.matrix[i+1][i+1]:
                break
            if i == self.size-2:
                if self.matrix[0][0] == 'X':
                    return 1
                elif self.matrix[0][0] == 'O':
                    return -1
        for i in range(self.size-1):
            if self.matrix[i][self.size-1-i] != self.matrix[i+1][self.size-2-i]:
                break
            if i == self.size-2:
                if self.matrix[0][self.size-1] == 'X':
                    return 1
                elif self.matrix[0][self.size-1] == 'O':
                    return -1

        return 0

    def get_cell(self, i, j):
        return self.matrix[i][j]

    def set_state(self, state):
        self.matrix = state

    def get_state(self):
        return self.matrix
    
    def get_size(self):
        return self.size

    def to_matrix(self):
        return self.matrix
