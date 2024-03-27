## 1. ¿Cuál es la implementación MÁS SENCILLA para representar un nodo?
class Node:
    def __init__(self, state, neighbor_states=[]):
        self.state = state
        self.neighbor_states = neighbor_states

def depth_first_search(initial_node, goal_state):
    stack = [initial_node]
    while stack:
        current_node = stack.pop()
        print(current_node.state)
        if current_node.state == goal_state:
            return True
        for neighbor_state in current_node.neighbor_states:
            stack.append(neighbor_state)
    return False

# def breadth_first_search(initial_node, goal_state):
#     queue = [initial_node]
#     while queue:
#         current_node = queue.pop(0)
#         print(current_node.state)
#         if current_node.state == goal_state:
#             return True
#         for child in current_node.children:
#             queue.append(child)
#     return False


## 4. ¿Qué problema tiene esta implementación?


if __name__ == "__main__":
    ## 2. ¿Cómo represento este grafo?

    # Option 1
    zero = Node('0', ['1', '3'])
    one = Node('1', ['0', '3', '2', '5'])
    two = Node('2', ['1', '3', '5', '4'])
    three = Node('3', ['0', '1', '2', '4'])
    four = Node('3', ['0', '1', '2', '4'])
    four = Node('3', ['0', '1', '2', '4'])
    ...

    graph = Graph([zero, one, two, three, ...])

    # Option 2
    graph_dict = {
        '0': ['1','3'],
        '1': ['0','2', '3', '5']
    }
    graph = Graph(graph_dict)



    print("Buscar en profundidad")
    # depth_first_search(zero, '5')

    print()

    print("Buscar en amplitud")
    # breadth_first_search(initial_node, '5')

