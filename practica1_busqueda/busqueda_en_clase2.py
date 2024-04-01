# Buenas prácticas y pequeños incrementos hacia la generalización

# 1. Renombrar clases y objetos de acuerdo al contexto de espacio de Estados
# 2. Eliminar código duplicado

# 3. Diseñar una clase para representar un EspacioDeEstados
#        Debe poder cargarse el grafo unidireccional de la practica #1
#        y el grafo bidireccional de la práctica #2 y #3

# 4. Ajusta las funciones de búsqueda para que
#       reciba un EspacioDeEstados, valor_inicial, valor_final
#       retornen el camino encontrado


class Stack():
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def is_empty(self):
        return len(self.values) == 0

class Queue():
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop(0)
    
    def is_empty(self):
        return len(self.values) == 0

class State:
    def __init__(self, value):
        self.value = value
        self.actions = []

    def add_action(self, action):
        if not action in self.actions:
            self.actions.append(action)

    def __str__(self):
        return f"{self.value} -> {self.actions}"


class StatesSpace:
    def __init__(self):
        self.space = {}

    def add_state(self, value):
        self.space[value] = State(value)

    def add_action(self, value1, value2):
        self.space[value1].add_action(value2)

    def get_state(self, value):
        return self.space[value]
    
    def __str__(self):
        return "\n".join(str(state) for state in self.space.values())


class Searcher:
    def __init__(self, space):
        self.space = space

    def depth_first(self, intial_value, goal_value):
        self.search(intial_value, goal_value, frontier=Stack())

    def breadth_first(self, intial_value, goal_value):
        self.search(intial_value, goal_value, frontier=Queue())

    def search(self, intial_value, goal_value, frontier):
        initial_state = self.space.get_state(intial_value)
        frontier.push(initial_state)
        while not frontier.is_empty():
            current_state = frontier.pop()
            print(current_state)
            if current_state.value == goal_value:
                print("Eureka!")
                return True
            for action in current_state.actions:
                next_state = self.space.get_state(action)
                frontier.push(next_state)
        return False



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
    goal_value = '6'

    print("Buscar en profundidad")
    searcher.depth_first(initial_value, goal_value)

    print("Buscar en amplitud")
    searcher.breadth_first(initial_value, goal_value)
