

class Cubie:
    def __init__(self, top=None, bot=None, front=None, back=None, left=None, right=None) -> None:
        self.top = top
        self.bot = bot
        self.front = front
        self.back = back
        self.left = left
        self.right = right

    def rotateZClockwise(self) -> None:
        self.top, self.back, self.bot, self.front = self.back, self.bot, self.front, self.top
    
    def rotateZCounterClockwise(self) -> None:
        self.top, self.back, self.bot, self.front = self.front, self.top, self.back, self.bot
    
    def rotateXClockwise(self) -> None:
        self.back, self.right, self.front, self.left = self.right, self.front, self.left, self.back
    
    def rotateXCounterClockwise(self) -> None:
        self.back, self.right, self.front, self.left = self.left, self.back, self.right, self.front
    
    def rotateYClockwise(self) -> None:
        self.top, self.right, self.bot, self.left = self.right, self.bot, self.left, self.top
    
    def rotateYCounterClockwise(self) -> None:
        self.top, self.right, self.bot, self.left = self.left, self.top, self.right, self.bot
    

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

    mike = Cube()

    mike.print()
    print(mike.isSolved())


if (__name__ == '__main__'):
    main()

