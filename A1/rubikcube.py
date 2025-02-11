

class Cubie:
    def __init__(self, top=None, bot=None, front=None, back=None, left=None, right=None) -> None:
        self.top = top
        self.bot = bot
        self.front = front
        self.back = back
        self.left = left
        self.right = right

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

    def __eq__(self, other):
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
        print(f'+---+---+---+')
        print(f'| {self.left} | {self.front} | {self.right} |')
        print(f'+---+---+---+')
        print(f'    | {self.bot} |')
        print(f'    +---+')
        print(f'    | {self.back} |')
        print(f'    +---+')

    

class Cube2:
    def __init__(self) -> None:
        
        #up
        self.UFL = Cubie(top='Y', front='B', left='O')
        self.UFR = Cubie(top='Y', front='B', right='R')

        self.UBL = Cubie(top='Y', back='G', left='O')
        self.UBR = Cubie(top='Y', back='G', right='R')

        #down
        self.DFL = Cubie(bot='W', front='B', left='O')
        self.DFR = Cubie(bot='W', front='B', right='R')

        self.DBL = Cubie(bot='w', back='G', left='O')
        self.DBR = Cubie(bot='W', back='G', right='R')

        # indexes based on x, y, z cords
        self.cubies = [
            [
                [self.DFL, self.UFL], 
                [self.DBL, self.UBL]
            ],
            [
                [self.DFR, self.UFR], 
                [self.DBR, self.UBR]
            ]
        ]
    

    def print(self) -> None:
        # print(f'      +-----+')
        # print(f'      | {self.cubies[0][1][1].top} {self.cubies[1][1][1].top} |')
        # print(f'      | {self.cubies[0][0][1].top} {self.cubies[1][0][1].top} |')
        # print(f'+-----+-----+-----+')
        # print(f'| {self.cubies[0][1][1].left} {self.cubies[0][0][1].left} | {self.cubies[0][0][1].front} {self.cubies[1][0][1].front} | {self.cubies[1][0][1].right} {self.cubies[1][1][1].right} |')
        # print(f'| {self.cubies[0][1][0].left} {self.cubies[0][0][0].left} | {self.cubies[0][0][0].front} {self.cubies[1][0][0].front} | {self.cubies[1][0][0].right} {self.cubies[1][1][0].right} |')
        # print(f'+-----+-----+-----+')
        # print(f'      | {self.cubies[0][0][0].bot} {self.cubies[1][0][0].bot} |')
        # print(f'      | {self.cubies[0][1][0].bot} {self.cubies[1][1][0].bot} |')
        # print(f'      +-----+')
        # print(f'      | {self.cubies[0][1][0].back} {self.cubies[1][1][0].back} |')
        # print(f'      | {self.cubies[0][1][1].back} {self.cubies[1][1][1].back} |')
        # print(f'      +-----+')

        print(f'      +-----+')
        print(f'      | {self.UBL.top} {self.UBR.top} |')
        print(f'      | {self.UFL.top} {self.UFR.top} |')
        print(f'+-----+-----+-----+')
        print(f'| {self.UBL.left} {self.UFL.left} | {self.UFL.front} {self.UFR.front} | {self.UFR.right} {self.UBR.right} |')
        print(f'| {self.DBL.left} {self.DFL.left} | {self.DFL.front} {self.DFR.front} | {self.DFR.right} {self.DBR.right} |')
        print(f'+-----+-----+-----+')
        print(f'      | {self.DFL.bot} {self.DFR.bot} |')
        print(f'      | {self.DBL.bot} {self.DBR.bot} |')
        print(f'      +-----+')
        print(f'      | {self.DBL.back} {self.DBR.back} |')
        print(f'      | {self.UBL.back} {self.UBR.back} |')
        print(f'      +-----+')


    def rotateFrontClockwise(self) -> None:
        self.UFL, self.UFR, self.DFR, self.DFL = self.DFL, self.UFL, self.UFR, self.DFR

        # self.cubies[0][0][1], self.cubies[1][0][1], self.cubies[1][0][0], self.cubies[0][0][0] = self.cubies[0][0][0], self.cubies[0][0][1], self.cubies[1][0][1], self.cubies[1][0][0]

        temp = [self.UFR, self.DFR, self.DFL, self.UFL]
        # temp = [self.cubies[0][0][1], self.cubies[1][0][1], self.cubies[1][0][0], self.cubies[0][0][0]]
        for i in temp:
            i.rotateYClockwise()


class Cube:
    def __init__(self) -> None:
        self.faceA: list[str] = ['W' for i in range(4)]
        self.faceB: list[str] = ['B' for i in range(4)]
        self.faceC: list[str] = ['R' for i in range(4)]
        self.faceD: list[str] = ['O' for i in range(4)]
        self.faceE: list[str] = ['G' for i in range(4)]
        self.faceF: list[str] = ['Y' for i in range(4)]

    def print(self) -> None:
        # print(f'      +-----+')
        # print(f'      | 0 1 |')
        # print(f'      | 2 3 |')
        # print(f'+-----+-----+-----+')
        # print(f'| 1 3 | 0 1 | 2 0 |')
        # print(f'| 0 2 | 2 3 | 3 1 |')
        # print(f'+-----+-----+-----+')
        # print(f'      | 3 2 |')
        # print(f'      | 1 0 |')
        # print(f'      +-----+')
        # print(f'      | 2 3 |')
        # print(f'      | 0 1 |')
        # print(f'      +-----+')

        # print(f'      +-----+')
        # print(f'      | {} {} |')
        # print(f'      | {} {} |')
        # print(f'+-----+-----+-----+')
        # print(f'| {} {} | {} {} | {} {} |')
        # print(f'| {} {} | {} {} | {} {} |')
        # print(f'+-----+-----+-----+')
        # print(f'      | {} {} |')
        # print(f'      | {} {} |')
        # print(f'      +-----+')
        # print(f'      | {} {} |')
        # print(f'      | {} {} |')
        # print(f'      +-----+')

        print(f'      +-----+')
        print(f'      | {self.faceC[0]} {self.faceC[1]} |')
        print(f'      | {self.faceC[2]} {self.faceC[3]} |')
        print(f'+-----+-----+-----+')
        print(f'| {self.faceB[1]} {self.faceB[3]} | {self.faceA[0]} {self.faceA[1]} | {self.faceD[2]} {self.faceD[0]} |')
        print(f'| {self.faceB[0]} {self.faceB[2]} | {self.faceA[2]} {self.faceA[3]} | {self.faceD[3]} {self.faceD[1]} |')
        print(f'+-----+-----+-----+')
        print(f'      | {self.faceE[3]} {self.faceE[2]} |')
        print(f'      | {self.faceE[1]} {self.faceE[0]} |')
        print(f'      +-----+')
        print(f'      | {self.faceF[2]} {self.faceF[3]} |')
        print(f'      | {self.faceF[0]} {self.faceF[1]} |')
        print(f'      +-----+')



    def reset(self) -> None:
        self.faceA: list[str] = ['W' for i in range(4)]
        self.faceB: list[str] = ['B' for i in range(4)]
        self.faceC: list[str] = ['R' for i in range(4)]
        self.faceD: list[str] = ['O' for i in range(4)]
        self.faceE: list[str] = ['G' for i in range(4)]
        self.faceF: list[str] = ['Y' for i in range(4)]

    def isSolved(self) -> bool:
        faces: list[list[str]] = [self.faceA, self.faceB, self.faceC, self.faceD, self.faceE, self.faceF]

        for face in faces:
            if(len(set(face)) != 1):
                return False
        else:
            return True

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
    
    def rotateFrontClockwise(self) -> None:
        pass
    
    def rotateFrontCounterClockwise(self) -> None:
        pass
    
    def rotateBackClockwise(self) -> None:
        pass
    
    def rotateBackCounterClockwise(self) -> None:
        pass



def main():

    mike = Cube2()
    mike.print()

    mike.rotateFrontClockwise()
    mike.print()



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

