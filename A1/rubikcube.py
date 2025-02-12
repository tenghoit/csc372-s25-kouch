

class Cubie:
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
    
    def rotateYCounterClockwise(self) -> None:
        self.top, self.right, self.bot, self.left = self.right, self.bot, self.left, self.top
    
    def rotateYClockwise(self) -> None:
        self.top, self.right, self.bot, self.left = self.left, self.top, self.right, self.bot

    def sameColorOrientation(self, other):
        if not isinstance(other, Cubie):
            return NotImplemented  # Ensure comparison only works with Cubie instances

        return (
            self.top == other.top and
            self.bot == other.bot and
            self.front == other.front and
            self.back == other.back and
            self.left == other.left and
            self.right == other.right
        )

    def print(self) -> None:
        print(f'    +---+')
        print(f'    | {self.top} |')
        print(f'+---+---+---+---+')
        print(f'| {self.left} | {self.front} | {self.right} | {self.back} |')
        print(f'+---+---+---+---+')
        print(f'    | {self.bot} |')
        print(f'    +---+')


class Cube:
    def __init__(self) -> None:
        
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

        # xyz cords of corner cubies
        self.positions = {
            'UFL': [0, 0, 1],
            'UFR': [1, 0, 1],
            'UBL': [0, 1, 1],
            'UBR': [1, 1, 1],
            'DFL': [0, 0, 0],
            'DFR': [1, 0, 0],
            'DBL': [0, 1, 0],
            'DBR': [1, 1, 0]
        }

    def reset(self) -> None:
        self.cubies = {
            'UFL': Cubie(top='Y', front='B', left='O', goalPosition=[0, 0, 1]),
            'UFR': Cubie(top='Y', front='B', right='R', goalPosition=[1, 0, 1]),
            'UBL': Cubie(top='Y', back='G', left='O', goalPosition=[0, 1, 1]),
            'UBR': Cubie(top='Y', back='G', right='R', goalPosition=[1, 1, 1]),
            'DFL': Cubie(bot='W', front='B', left='O', goalPosition=[0, 0, 0]),
            'DFR': Cubie(bot='W', front='B', right='R', goalPosition=[1, 0, 0]),
            'DBL': Cubie(bot='w', back='G', left='O', goalPosition=[0, 1, 0]),
            'DBR': Cubie(bot='W', back='G', right='R', goalPosition=[1, 1, 0])
        }
    

    def print(self) -> None:

        print(f'      +-----+')
        print(f'      | {self.cubies['UBL'].top} {self.cubies['UBR'].top} |')
        print(f'      | {self.cubies['UFL'].top} {self.cubies['UFR'].top} |')
        print(f'+-----+-----+-----+')
        print(f'| {self.cubies['UBL'].left} {self.cubies['UFL'].left} | {self.cubies['UFL'].front} {self.cubies['UFR'].front} | {self.cubies['UFR'].right} {self.cubies['UBR'].right} |')
        print(f'| {self.cubies['DBL'].left} {self.cubies['DFL'].left} | {self.cubies['DFL'].front} {self.cubies['DFR'].front} | {self.cubies['DFR'].right} {self.cubies['DBR'].right} |')
        print(f'+-----+-----+-----+')
        print(f'      | {self.cubies['DFL'].bot} {self.cubies['DFR'].bot} |')
        print(f'      | {self.cubies['DBL'].bot} {self.cubies['DBR'].bot} |')
        print(f'      +-----+')
        print(f'      | {self.cubies['DBL'].back} {self.cubies['DBR'].back} |')
        print(f'      | {self.cubies['UBL'].back} {self.cubies['UBR'].back} |')
        print(f'      +-----+')

    def isSolved(self) -> None:
        pass

    def __rotateClockwise(self, positions) -> None:
        
        if len(positions) < 2:
            raise ValueError("You need at least two cubies to swap.")

        # save last elem
        lastElem = self.cubies[positions[-1]]

        # start from end, go backward, overwrite
        for i in range(len(positions) - 1, 0, -1):
            self.cubies[positions[i]] = self.cubies[positions[i-1]]

        self.cubies[positions[0]] = lastElem

    def __rotateCounterClockwise(self, positions) -> None:
        
        if len(positions) < 2:
            raise ValueError("You need at least two cubies to swap.")

        # save first elem
        firstElem = self.cubies[positions[0]]

        # start from 0, replace with next
        for i in range(0, len(positions) - 1):
            self.cubies[positions[i]] = self.cubies[positions[i+1]]

        self.cubies[positions[-1]] = firstElem


    def rotateFrontClockwise(self) -> None:
        # self.cubies['UFL'], self.cubies['UFR'], self.cubies['DFR'], self.cubies['DFL'] = self.cubies['DFL'], self.cubies['UFL'], self.cubies['UFR'], self.cubies['DFR']

        positions = ['UFL', 'UFR', 'DFR', 'DFL']
        self.__rotateClockwise(positions)

        # temp = [self.cubies['UFR'], self.cubies['DFR'], self.cubies['DFL'], self.cubies['UFL']]

        for i in positions:
            self.cubies[i].rotateYClockwise()


    def rotateFrontCounterClockwise(self) -> None:
        # self.cubies['UFL'], self.cubies['UFR'], self.cubies['DFR'], self.cubies['DFL'] = self.cubies['UFR'], self.cubies['DFR'], self.cubies['DFL'], self.cubies['UFL']

        positions = ['UFL', 'UFR', 'DFR', 'DFL']
        self.__rotateCounterClockwise(positions)

        # temp = [self.cubies['UFL'], self.cubies['UFR'], self.cubies['DFR'], self.cubies['DFL']]
        for i in positions:
            self.cubies[i].rotateYCounterClockwise()

    def rotateBackClockwise(self) -> None:
        positions = ['UBL', 'UBR', 'DBR', 'DBL']
        self.__rotateCounterClockwise(positions)

        for i in positions:
            self.cubies[i].rotateYCounterClockwise()

    
    def rotateBackCounterClockwise(self) -> None:
        pass

    def rotateBottomClockwise(self) -> None:
        pass
    
    def rotateBottomCounterClockwise(self) -> None:
        pass
    
    def rotateTopClockwise(self) -> None:
        pass
    
    def rotateTopCounterClockwise(self) -> None:
        pass
    
    def rotateLeftClockwise(self) -> None:
        pass
    
    def rotateLeftCounterClockwise(self) -> None:
        pass
    
    def rotateRightClockwise(self) -> None:
        pass
    
    def rotateRightCounterClockwise(self) -> None:
        pass


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


        operation = int(input('\nSelect: '))

        if(operation == 0):
            break
        elif(operation == 1): 
            blocky.rotateFrontClockwise()
        elif(operation == 2): 
            blocky.rotateFrontCounterClockwise()
        elif(operation == 3): 
            blocky.rotateBackClockwise()
        elif(operation == 4): 
            blocky.rotateBackCounterClockwise()
        elif(operation == 5): 
            blocky.rotateTopClockwise()
        elif(operation == 6): 
            blocky.rotateTopCounterClockwise()
        elif(operation == 7): 
            blocky.rotateBottomClockwise()
        elif(operation == 8): 
            blocky.rotateBottomCounterClockwise()
        elif(operation == 9): 
            blocky.rotateLeftClockwise()
        elif(operation == 10): 
            blocky.rotateLeftCounterClockwise()
        elif(operation == 11): 
            blocky.rotateRightClockwise()
        elif(operation == 12): 
            blocky.rotateRightCounterClockwise()
        else:
            print('Invalid Operation.')
        
            
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


if (__name__ == '__main__'):
    main()
    # cubieTest()

