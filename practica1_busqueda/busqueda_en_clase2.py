# Buenas prácticas y pequeños incrementos hacia la generalización

# 1. Renombrar clases y objetos de acuerdo al contexto de espacio de Estados
# 2. Eliminar código duplicado

# 3. Diseñar una clase para representar un EspacioDeEstados
#        Debe poder cargarse el grafo unidireccional de la practica #1
#        y el grafo bidireccional de la práctica #2 y #3

# 4. Ajusta las funciones de búsqueda para que
#       reciba un EspacioDeEstados, valor_inicial, valor_final
#       retornen el camino encontrado

class Frontier():
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def has(self, value):
        return value in self.values

    def is_empty(self):
        return len(self.values) == 0

class Stack(Frontier):
    def pop(self):
        return self.values.pop()

class Queue(Frontier):
    def pop(self):
        return self.values.pop(0)

class State:
    def __init__(self, value):
        self.value = value
        self.actions = []
        self.visited = False
        self.parent = None

    def add_action(self, action):
        if not action in self.actions:
            self.actions.append(action)

    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def was_visited(self):
        return self.visited
    
    def set_parent(self, value):
        self.parent = value

    def __str__(self):
        return f"{self.value}:{self.visited} -> {self.actions}"


class StatesSpace:
    def __init__(self):
        self.space = {}

    def add_state(self, value):
        self.space[value] = State(value)

    def add_action(self, value1, value2):
        self.space[value1].add_action(value2)

    def get_state(self, value):
        return self.space[value]

    def reset_visited(self):
        for state in self.space.values():
            state.mark_unvisited()

    def __str__(self):
        return "\n".join(str(state) for state in self.space.values())


class Searcher:
    def __init__(self, space):
        self.space = space

    def depth_first(self, intial_value, goal_value):
        return self.search(intial_value, goal_value, frontier=Stack())

    def breadth_first(self, intial_value, goal_value):
        return self.search(intial_value, goal_value, frontier=Queue())

    def search(self, intial_value, goal_value, frontier):
        initial_state = self.space.get_state(intial_value)
        frontier.push(initial_state)

        while not frontier.is_empty():
            current_state = frontier.pop()
            # print(current_state)
            current_state.mark_visited()

            if current_state.value == goal_value:
                return self.build_solution_path(current_state)

            for action in current_state.actions:
                next_state = self.space.get_state(action)
                if not next_state.was_visited() and not frontier.has(next_state):
                    next_state.set_parent(current_state)
                    frontier.push(next_state)

        return []

    def build_solution_path(self, state):
        path = []
        while state:
            path.append(state.value)
            state = state.parent
        return list(reversed(path))



if __name__ == "__main__":
    # space_dict = {
    #     'A': ['B', 'C'],
    #     'B': ['D', 'E'],
    #     'C': ['F'],
    #     'D': [],
    #     'E': [],
    #     'F': []
    # }
    space_dict = {
        '0': ['1', '3'],
        '1': ['0', '2', '3', '5'],
        '2': ['1', '3', '5', '4'],
        '3': ['0', '1', '2', '4'],
        '4': ['2', '3', '6'],
        '5': ['1', '2'],
        '6': ['1', '4'],
    }

    space = StatesSpace()

    state_values = space_dict.keys()
    for state_value in state_values:
        space.add_state(state_value)

    for state_value, state_actions in space_dict.items():
        for action in state_actions:
            space.add_action(state_value, action)

    searcher = Searcher(space)
    # print(space)

    initial_value = '0'
    goal_value = '5'

    print("Buscar en profundidad")
    path = searcher.depth_first(initial_value, goal_value)
    print(path)

    space.reset_visited()

    print("Buscar en amplitud")
    path = searcher.breadth_first(initial_value, goal_value)
    print(path)
