## 1. ¿Cuál es la implementación MÁS SENCILLA para representar un nodo?
class Node:
    def __init__(self, state, children=[]):
        self.state = state
        self.children = children

## 3. Qué "signature" necesitan las funciones de búsqueda?
  # Entradas (initial_state, goal_stat)
  # Salidas: OK: return True
            # No Solution: False

def depth_first_search(initial_node, goal_state):
    stack = [initial_node]
    while stack:
        current_node = stack.pop()
        print(current_node.state)
        if current_node.state == goal_state:
            return True
        for child in current_node.children:
            stack.append(child)
    return False

def breadth_first_search(initial_node, goal_state):
    queue = [initial_node]
    while queue:
        current_node = queue.pop(0)
        print(current_node.state)
        if current_node.state == goal_state:
            return True
        for child in current_node.children:
            queue.append(child)
    return False


## 4. ¿Qué problema tiene esta implementación?


if __name__ == "__main__":
    ## 2. ¿Cómo represento este grafo?
    initial_node = Node("A",
        [
            Node("B", [
                Node("D"),
                Node("E")
            ]),
            Node("C", [
                Node("F")
            ])
        ]
    )

    print("Buscar en profundidad")
    depth_first_search(initial_node, 'E')

    print()

    print("Buscar en amplitud")
    breadth_first_search(initial_node, 'E')

    # 1. ¿Y si mi grafo es bidireccional? -> Necesito una manera de recordar qué nodos visité
    # 2. Uy, solo estoy imprimpiendo los nodos visitados, 
    #     necesito una forma de recordar el camino y reutilizarlo de ser necesario.
