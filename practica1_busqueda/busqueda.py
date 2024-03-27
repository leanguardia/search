

class Node:
    def __init__(self, state, children=[]):
        self.state = state
        self.children = children

def breadth_first_search(initial_node, goal_state):
    queue = [initial_node]
    while queue:
        current_node = queue.pop(0)
        print(current_node.state)
        if current_node.state == goal_state:
            print("Eureka!")
            return True
        for child in current_node.children:
            queue.append(child)

def depth_first_search(initial_node, goal_state):
    stack = [initial_node]
    print(stack[0])
    while stack:
        current_node = stack.pop()
        print(current_node.state)
        if current_node.state == goal_state:
            print("Eureka!")
            return True
        for child in reversed(current_node.children):
            stack.append(child)


# __name__ (special variable) is set to "__main__" when it is read from standard input or a script
if __name__ == "__main__":
    initial_node = Node(
        'A', [
            Node('B',
                [Node('D'), Node('E')]
            ), 
            Node('C', 
                 [Node('F')]
            )
        ]
    )
    print("Buscando en amplitud")
    breadth_first_search(initial_node, 'E')

    print()

    print("Buscando en profundidad")
    depth_first_search(initial_node, 'E')


    # -- ¿BIDIRECCIONALIDAD?
    # -- ¿Costos?
    # -- REconstrucción de camino?
    # -- Genérico?
