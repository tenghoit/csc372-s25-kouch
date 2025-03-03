from rubikcube import Cubie, Cube

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
        self.explored = [self.root]
        self.frontier = []


    def breadth_first_search(self) -> list[str]:

        # start initial frontier
        for move in Cube.moves.keys(): 
            new_state = self.root.state.turn_and_clone(move)
            self.frontier.append(Node(self.root, new_state, move))

        
        while len(self.frontier) != 0:

            print(f'Explored: {len(self.explored)} | Frontier: {len(self.frontier)}')

            current_node = self.frontier.pop(0)

            seen = False

            # check if seen already
            for node in self.explored:
                if current_node.state.is_same(node.state) == True:
                    print(current_node.state.is_same(node.state))
                    seen = True
                    break

            if seen == True:
                continue

            # check if solved
            if current_node.state.is_solved() == True:
                return current_node.get_action_sequence()

            # generate nodes
            for move in Cube.moves.keys():

                if move == Cube.opposite_moves[current_node.action]:
                    continue
                
                new_state = current_node.state.turn_and_clone(move)

                self.frontier.append(Node(current_node, new_state, move))

            self.explored.append(current_node)


    def iterative_deepening_depth_first_search(self) -> list[str]:

        depth = 0

        while True:

            result = self.depth_limited_search(self.root, depth)
                
            if result is not None:
                return result
            
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

    # result = solution.breadth_first_search()
    # print(result)

    result = solution.iterative_deepening_depth_first_search()
    print(result)






if (__name__ == '__main__'):
    main()