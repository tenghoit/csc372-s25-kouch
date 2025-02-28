from rubikcube import Cubie, Cube

class Node:
    def __init__(self, parent, state, action) -> None:
        self.parent: Node = parent
        self.state: Cube = state
        self.action = action

    def getActionSequence(self):
        """
        Returns action sequence for a given state
        """

        sequence = []
        currentNode = self
        
        while currentNode.parent is not None:

            sequence.append(currentNode.action)

            currentNode = currentNode.parent

        return sequence.reverse()

    def getPathCost(self) -> int:
        """
        Returns path cost for a given state
        """
        pathCost = 0
        currentNode = self

        while currentNode.parent is not None:

            pathCost += 1

            currentNode = currentNode.parent

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

    def __init__(self, state) -> None:
        self.root = Node(parent=None, state=state, action=None)
        self.explored = [self.root]
        self.frontier = []

        # start initial frontier
        for move in Cube.moves.keys(): 
            new_state = self.root.state.turn_and_clone(move)
            self.frontier.append(Node(self.root, new_state, move))
        

    def breadthFirstSearch(self) -> list[str]:
        
        while len(self.frontier) != 0:

            currentNode = self.frontier.pop(0)

            if currentNode.state.is_solved() == True:
                return currentNode.getActionSequence()

            for move in Cube.moves.keys():

                if move == Cube.opposite_moves[currentNode.action]:
                    continue
                
                new_state = currentNode.state.turn_and_clone(move)

                self.frontier.append(Node(currentNode, new_state, move))

            self.explored.append(currentNode)



def main():
    blocky = Cube()
    blocky.print()
    blocky.randomize(5)
    blocky.print()

    solution = Solution(blocky)

    # result = solution.breadthFirstSearch()

    print(result)






if (__name__ == '__main__'):
    main()