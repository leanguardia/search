

class State:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.actions = []
    
    def add_action(self, other_value):
        if not other_value in self.actions:
            self.actions.append(other_value)

    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def __str__(self):
        return f"{self.value}, visited:{self.visited} -> {self.actions}"


def breadth_first_search(space, initial_value, end_value):
    queue = [space.get_state(initial_value)]
    while queue:
        current_state = queue.pop(0)
        print(current_state)
        current_state.mark_visited()
        if current_state.value == end_value:
            print("Eureka!")
            return True
        for action in current_state.actions:
            next_state = space.get_state(action)
            if not next_state.visited:
                queue.append(next_state)

def depth_first_search(space, initial_value, end_value):
    stack = [space.get_state(initial_value)]
    while stack:
        current_state = stack.pop()
        print(current_state)
        current_state.mark_visited()
        if current_state.value == end_value:
            print("Eureka")
            return True
        for action in reversed(current_state.actions):
            next_state = space.get_state(action)
            if not next_state.visited:
                stack.append(next_state)

class StateSpace():
    def __init__(self):
        self.states = {}

    def add_state(self, state):
        self.states[state.value] = state

    def get_state(self, value):
        return self.states[value]

    def add_edge(self, value1, value2):
        self.states[value1].add_action(value2)

    def reset(self):
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

    print("Buscar en profundidad")
    depth_first_search(space, '0', '5')

    space.reset()

    print("Buscar en amplitud")
    breadth_first_search(space, '0', '5')

