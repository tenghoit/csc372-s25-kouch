

class Cubie:
    """
    Represent a single cubie with 6 sides.
    """

    def __init__(self, top=None, bot=None, front=None, back=None, left=None, right=None, goalPosition: list[int]=None) -> None:
        self.top = top
        self.bot = bot
        self.front = front
        self.back = back
        self.left = left
        self.right = right
        self.goalPosition: list[int] = goalPosition

    def rotateXCounterClockwise(self) -> None:
        self.top, self.back, self.bot, self.front = self.back, self.bot, self.front, self.top
    
    def rotateXClockwise(self) -> None:
        self.top, self.back, self.bot, self.front = self.front, self.top, self.back, self.bot
    
    def rotateZCounterClockwise(self) -> None:
        self.back, self.right, self.front, self.left = self.right, self.front, self.left, self.back
    
    def rotateZClockwise(self) -> None:
        self.back, self.right, self.front, self.left = self.left, self.back, self.right, self.front
    
    def rotateYClockwise(self) -> None:
        self.top, self.right, self.bot, self.left = self.right, self.bot, self.left, self.top
    
    def rotateYCounterClockwise(self) -> None:
        self.top, self.right, self.bot, self.left = self.left, self.top, self.right, self.bot

    def sameColorOrientation(self, other) -> bool:
        """
        Compare if two cubie has the same color orientation.
        """

        if not isinstance(other, Cubie):
            return NotImplemented

        for side in ['top', 'bot', 'front', 'back', 'left', 'right']:
            self_side = getattr(self, side)
            other_side = getattr(other, side)

            # ensure both side are None or not None
            if (self_side is None) != (other_side is None):
                return False

            # If not None, then must match
            if self_side is not None and self_side != other_side:
                return False

        return True


    def print(self) -> None:
        print(f'    +---+')
        print(f'    | {self.top} |')
        print(f'+---+---+---+---+')
        print(f'| {self.left} | {self.front} | {self.right} | {self.back} |')
        print(f'+---+---+---+---+')
        print(f'    | {self.bot} |')
        print(f'    +---+')

    def clone(self) -> 'Cubie':
        """
        Return a new deep copy of cubie 
        """
        return Cubie(
            top = self.top,
            bot = self.bot,
            front = self.front,
            back = self.back,
            left = self.left,
            right = self.right,
            goalPosition=self.goalPosition
        )


class Cube:
    """
    Represent a Cube that is maded up of cubies.
    """

    solvedCube = {
        'UFL': Cubie(top='Y', front='B', left='O', goalPosition=[0, 0, 1]),
        'UFR': Cubie(top='Y', front='B', right='R', goalPosition=[1, 0, 1]),
        'UBL': Cubie(top='Y', back='G', left='O', goalPosition=[0, 1, 1]),
        'UBR': Cubie(top='Y', back='G', right='R', goalPosition=[1, 1, 1]),
        'DFL': Cubie(bot='W', front='B', left='O', goalPosition=[0, 0, 0]),
        'DFR': Cubie(bot='W', front='B', right='R', goalPosition=[1, 0, 0]),
        'DBL': Cubie(bot='W', back='G', left='O', goalPosition=[0, 1, 0]),
        'DBR': Cubie(bot='W', back='G', right='R', goalPosition=[1, 1, 0])
    }
    
    # xyz cords of corner cubies
    positions = {
        'UFL': [0, 0, 1],
        'UFR': [1, 0, 1],
        'UBL': [0, 1, 1],
        'UBR': [1, 1, 1],
        'DFL': [0, 0, 0],
        'DFR': [1, 0, 0],
        'DBL': [0, 1, 0],
        'DBR': [1, 1, 0]
    }

    def __init__(self) -> None:

        # anchor cubie will be UFR
        
        self.cubies = {
            'UFL': Cubie(top='Y', front='B', left='O', goalPosition=[0, 0, 1]),
            'UFR': Cubie(top='Y', front='B', right='R', goalPosition=[1, 0, 1]),
            'UBL': Cubie(top='Y', back='G', left='O', goalPosition=[0, 1, 1]),
            'UBR': Cubie(top='Y', back='G', right='R', goalPosition=[1, 1, 1]),
            'DFL': Cubie(bot='W', front='B', left='O', goalPosition=[0, 0, 0]),
            'DFR': Cubie(bot='W', front='B', right='R', goalPosition=[1, 0, 0]),
            'DBL': Cubie(bot='W', back='G', left='O', goalPosition=[0, 1, 0]),
            'DBR': Cubie(bot='W', back='G', right='R', goalPosition=[1, 1, 0])
        }


    def reset(self) -> None:
        """
        Reset cube back to solved state.
        """
        for key in Cube.solvedCube.keys():
            self.cubies[key] = Cube.solvedCube[key].clone()
    

    def print(self) -> None:

        print(f'      +-----+')
        print(f'      | {self.cubies['UBL'].top} {self.cubies['UBR'].top} |')
        print(f'      | {self.cubies['UFL'].top} {self.cubies['UFR'].top} |')
        print(f'+-----+-----+-----+-----+')
        print(f'| {self.cubies['UBL'].left} {self.cubies['UFL'].left} | {self.cubies['UFL'].front} {self.cubies['UFR'].front} | {self.cubies['UFR'].right} {self.cubies['UBR'].right} | {self.cubies['UBR'].back} {self.cubies['UBL'].back} |')
        print(f'| {self.cubies['DBL'].left} {self.cubies['DFL'].left} | {self.cubies['DFL'].front} {self.cubies['DFR'].front} | {self.cubies['DFR'].right} {self.cubies['DBR'].right} | {self.cubies['DBR'].back} {self.cubies['DBL'].back} |')
        print(f'+-----+-----+-----+-----+')
        print(f'      | {self.cubies['DFL'].bot} {self.cubies['DFR'].bot} |')
        print(f'      | {self.cubies['DBL'].bot} {self.cubies['DBR'].bot} |')
        print(f'      +-----+')

    def isSolved(self) -> bool:
        """
        Check if cube is in a solved state
        """

        for key in Cube.solvedCube.keys():
            if(self.cubies[key].sameColorOrientation(Cube.solvedCube[key]) == False):
                return False

        return True

    def getHeuristicScore(self) -> int:
        """
        Returns heuristic score of the current state. Combination of:
            * manhattan dist between current position and goal position of each cubie
            * color orientation
        """

        totalScore = 0

        for key in self.cubies.keys():

            goalPosition = self.cubies[key].goalPosition
            currentPosition = Cube.positions[key]

            manhattanDist = 0

            for i in range(3):
                manhattanDist += abs( goalPosition[i] - currentPosition[i] )



            totalScore += manhattanDist



    def __rotateClockwise(self, positions) -> None:
        """
        A Private function that rotate faces clockwise. 
        ie 1, 2, 3, 4 = 4, 1, 2, 3 
        """
        
        if len(positions) < 2:
            raise ValueError("You need at least two cubies to swap.")

        # save last elem
        lastElem = self.cubies[positions[-1]]

        # start from end, go backward, overwrite
        for i in range(len(positions) - 1, 0, -1):
            self.cubies[positions[i]] = self.cubies[positions[i-1]]

        self.cubies[positions[0]] = lastElem


    def __rotateCounterClockwise(self, positions) -> None:
        """
        A Private function that rotate faces counter clockwise. 
        ie 1, 2, 3, 4 = 2, 3, 4, 1
        """
        
        if len(positions) < 2:
            raise ValueError("You need at least two cubies to swap.")

        # save first elem
        firstElem = self.cubies[positions[0]]

        # start from 0, replace with next
        for i in range(0, len(positions) - 1):
            self.cubies[positions[i]] = self.cubies[positions[i+1]]

        self.cubies[positions[-1]] = firstElem



    def __rotateXClosewise(self) -> None:
        positions = ['UFL', 'UBL', 'DBL', 'DFL']
        self.__rotateCounterClockwise(positions)
        for i in positions:
            self.cubies[i].rotateXCounterClockwise()

    def __rotateXCounterClosewise(self) -> None:
        positions = ['UFL', 'UBL', 'DBL', 'DFL']
        self.__rotateClockwise(positions)
        for i in positions:
            self.cubies[i].rotateXClockwise()

    def __rotateYClosewise(self) -> None:
        positions = ['UBR', 'UBL', 'DBL', 'DBR']
        self.__rotateClockwise(positions)
        for i in positions:
            self.cubies[i].rotateYClockwise()

    def __rotateYCounterClosewise(self) -> None:
        positions = ['UBR', 'UBL', 'DBL', 'DBR']
        self.__rotateCounterClockwise(positions)
        for i in positions:
            self.cubies[i].rotateYCounterClockwise()
    
    def __rotateZClosewise(self) -> None:
        positions = ['DFL', 'DFR', 'DBR', 'DBL']
        self.__rotateClockwise(positions)
        for i in positions:
            self.cubies[i].rotateZCounterClockwise()

    def __rotateZCounterClosewise(self) -> None:
        positions = ['DFL', 'DFR', 'DBR', 'DBL']
        self.__rotateCounterClockwise(positions)
        for i in positions:
            self.cubies[i].rotateZClockwise()

    

    def rotateFrontClockwise(self) -> None:
        self.__rotateYClosewise()

    def rotateFrontCounterClockwise(self) -> None:
        self.__rotateYCounterClosewise()

    def rotateBackClockwise(self) -> None:
        self.__rotateYClosewise()
    
    def rotateBackCounterClockwise(self) -> None:
        self.__rotateYCounterClosewise()

    def rotateBottomClockwise(self) -> None:
        self.__rotateZClosewise()
    
    def rotateBottomCounterClockwise(self) -> None:
        self.__rotateZCounterClosewise()
    
    def rotateTopClockwise(self) -> None:
        self.__rotateZClosewise()
    
    def rotateTopCounterClockwise(self) -> None:
        self.__rotateZCounterClosewise()
    
    def rotateLeftClockwise(self) -> None:
        self.__rotateXClosewise()
    
    def rotateLeftCounterClockwise(self) -> None:
        self.__rotateXCounterClosewise()
    
    def rotateRightClockwise(self) -> None:
        self.__rotateXClosewise()
    
    def rotateRightCounterClockwise(self) -> None:
        self.__rotateXCounterClosewise()


def main():

    print('\n2x2 Rubik\'s cube')
    blocky = Cube()

    while(True):

        print('')
        blocky.print()

        print('\nOperations:')
        print('0: Exit')
        print('1: Rotate Front Clockwise')
        print('2: Rotate Front Counterclockwise')
        print('3: Rotate Back Clockwise')
        print('4: Rotate Back Counterclockwise')
        print('5: Rotate Top Clockwise')
        print('6: Rotate Top Counterclockwise')
        print('7: Rotate Bottom Clockwise')
        print('8: Rotate Bottom Counterclockwise')
        print('9: Rotate Left Clockwise')
        print('10: Rotate Left Counterclockwise')
        print('11: Rotate Right Clockwise')
        print('12: Rotate Right Counterclockwise')
        print('13: Check isSolved')

        try:
            operation = int(input('\nSelect: '))

            if operation == 0:
                print("Exiting program.")
                break
            elif operation == 1: 
                blocky.rotateFrontClockwise()
            elif operation == 2: 
                blocky.rotateFrontCounterClockwise()
            elif operation == 3: 
                blocky.rotateBackClockwise()
            elif operation == 4: 
                blocky.rotateBackCounterClockwise()
            elif operation == 5: 
                blocky.rotateTopClockwise()
            elif operation == 6: 
                blocky.rotateTopCounterClockwise()
            elif operation == 7: 
                blocky.rotateBottomClockwise()
            elif operation == 8: 
                blocky.rotateBottomCounterClockwise()
            elif operation == 9: 
                blocky.rotateLeftClockwise()
            elif operation == 10: 
                blocky.rotateLeftCounterClockwise()
            elif operation == 11: 
                blocky.rotateRightClockwise()
            elif operation == 12: 
                blocky.rotateRightCounterClockwise()
            elif operation == 13: 
                print(blocky.isSolved())
            else:
                print('Invalid Operation.')
        except ValueError:
            print("Please enter a valid number.")
        
            
def cubieTest():
    sam = Cubie(top='Y', bot='W', front='B', back='G', left='O', right='R')
    sam.print()

    sam.rotateYClockwise()
    sam.print()
    sam.rotateYCounterClockwise()
    sam.print()

    sam.rotateXClockwise()
    sam.print()
    sam.rotateXCounterClockwise()
    sam.print()

    sam.rotateZClockwise()
    sam.print()
    sam.rotateZCounterClockwise()
    sam.print()

    lad = Cubie(top='Y', bot='W', front='B', back='G', left='O')

    print(sam.sameColorOrientation(lad))

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

        

class Solution:
    rotations = ['D', 'D', 'L', 'L', 'B', 'B']

    def __init__(self, root) -> None:
        self.root = Node(parent=None, state=root, action=None)
        self.explored = []
        self.frontier = []
        

    def breadthFirstSearch(self):
        
        
        while len(self.frontier) != 0:

            currentNode = self.frontier.pop(0)



    





if (__name__ == '__main__'):
    main()
    # cubieTest()

