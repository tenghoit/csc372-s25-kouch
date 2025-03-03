from rubikcube import Cubie, Cube
import time

class Node:
    def __init__(self, parent, state, action) -> None:
        self.parent: Node = parent
        self.state: Cube = state
        self.action = action

    def get_action_sequence(self):
        """
        Returns action sequence for a given state
        """

        sequence = []
        current_node = self
        
        while current_node.parent is not None:

            sequence.append(current_node.action)

            current_node = current_node.parent

        sequence.reverse()
        return sequence


    def get_path_cost(self) -> int:
        """
        Returns path cost for a given state
        """
        pathCost = 0
        current_node = self

        while current_node.parent is not None:

            pathCost += 1

            current_node = current_node.parent

        return pathCost


class PriorityQueue:
    """
    Priority queue using a heap
    """
    def __init__(self) -> None:
        self.queue = []

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        
        return False
        

class Solution:

    def __init__(self, state: Cube) -> None:
        self.root = Node(parent=None, state=state, action=None)


    def breadth_first_search(self) -> list[str]:

        start_time = time.process_time()

        explored = set()
        explored.add(self.root.state)
        frontier = []

        # start initial frontier
        for move in Cube.moves.keys(): 
            new_state = self.root.state.turn_and_clone(move)
            frontier.append(Node(self.root, new_state, move))

        
        while len(frontier) != 0:

            # print(f'Explored: {len(explored)} | Frontier: {len(frontier)}')

            current_node = frontier.pop(0)

            if current_node.state in explored:
                continue

            # check if solved
            if current_node.state.is_solved() == True:
                end_time = time.process_time()
                sequence = current_node.get_action_sequence()
                return [sequence, end_time-start_time]

            # generate nodes
            for move in Cube.moves.keys():

                if move == Cube.opposite_moves[current_node.action]:
                    continue
                
                new_state = current_node.state.turn_and_clone(move)

                frontier.append(Node(current_node, new_state, move))

            explored.add(current_node.state)


    def iterative_deepening_depth_first_search(self) -> list[str]:
        
        start_time = time.process_time()
        depth = 0

        while True:

            result = self.depth_limited_search(self.root, depth)
                
            if result is not None:
                end_time = time.process_time()
                return [result, end_time-start_time]
            
            depth += 1

                

    def depth_limited_search(self, current_node, depth_limit) -> list[str]:
        
        if(current_node.state.is_solved() == True):
            return current_node.get_action_sequence()

        if depth_limit == 0:
            return None

        # generate nodes
        for move in Cube.moves.keys():

            if (current_node.action is not None) and (move == Cube.opposite_moves[current_node.action]):
                continue
            
            new_state = current_node.state.turn_and_clone(move)

            new_node = Node(current_node, new_state, move)

            result = self.depth_limited_search(new_node, depth_limit - 1)

            # success return
            if result is not None:
                return result

        #failure
        return None



def main():
    blocky = Cube()
    blocky.print()
    sequence = blocky.randomize(8)
    print(sequence)
    blocky.print()

    solution = Solution(blocky)

    result = solution.breadth_first_search()
    print(f'BFS: {result[0]} | Time: {result[1]}')

    result = solution.iterative_deepening_depth_first_search()
    print(f'IDDFS: {result[0]} | Time: {result[1]}')






if (__name__ == '__main__'):
    main()