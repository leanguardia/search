

class State:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.actions = []
        self.parent = None
    
    def add_action(self, other_value):
        if not other_value in self.actions:
            self.actions.append(other_value)

    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def set_parent(self, parent):
        self.parent = parent

    def __str__(self):
        return f"{self.value}, visited:{self.visited} -> {self.actions}"


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def remove(self):
        return self.queue.pop(0)
    
    def has(self, value):
        return value in self.queue

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def remove(self):
        return self.stack.pop()
    
    def has(self, value):
        return value in self.stack


class Searcher:
    def __init__(self, space):
        self.space = space

    def search(self, initial_value, end_value, data_structure):
        initial_state = self.space.get_state(initial_value)
        data_structure.push(initial_state)

        while data_structure:
            current_state = data_structure.remove()
            current_state.mark_visited()

            if current_state.value == end_value:
                return self.build_solution_path(current_state)

            for action in current_state.actions:
                next_state = self.space.get_state(action)
                if not next_state.visited and not data_structure.has(next_state):
                    next_state.set_parent(current_state)
                    data_structure.push(next_state)
        return []

    def breadth_first(self, initial_value, end_value):
        return self.search(initial_value, end_value, Queue())

    def depth_first(self, initial_value, end_value):
        return self.search(initial_value, end_value, Stack())
    
    def build_solution_path(self, state):
        path = []
        while state:
            path.append(state.value)
            state = state.parent
        return list(reversed(path))

class StateSpace():
    def __init__(self):
        self.states = {}

    def add_state(self, state):
        self.states[state.value] = state

    def get_state(self, value):
        return self.states[value]

    def add_edge(self, value1, value2):
        self.states[value1].add_action(value2)

    def reset_visits(self):
        for state in self.states.values():
            state.mark_unvisited()


if __name__ == "__main__":
    graph_dict = {
        '0': ['1', '3'],
        '1': ['0', '2', '3', '5'],
        '2': ['1', '3', '5', '4'],
        '3': ['0', '1', '2', '4'],
        '4': ['2', '3', '6'],
        '5': ['1', '2'],
        '6': ['1', '4'],
    }
    state_values = graph_dict.keys()

    space  = StateSpace()

    for value in state_values:
        space.add_state(State(value))

    for state, actions in graph_dict.items():
        for action in actions:
            space.add_edge(state, action)

    searcher = Searcher(space)

    print("Buscando en Profundidad")
    print(searcher.depth_first('0', '6'))

    space.reset_visits()

    print("Buscando en amplitud")
    print(searcher.breadth_first('0', '6'))
