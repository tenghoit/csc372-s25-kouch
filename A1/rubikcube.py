

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



    def reset(self):
        self.faceA: list[str] = ['W' for i in range(4)]
        self.faceB: list[str] = ['B' for i in range(4)]
        self.faceC: list[str] = ['R' for i in range(4)]
        self.faceD: list[str] = ['O' for i in range(4)]
        self.faceE: list[str] = ['G' for i in range(4)]
        self.faceF: list[str] = ['Y' for i in range(4)]

    def turn(self):
        pass



def main():

    micky = Cube()

    micky.print()


if (__name__ == '__main__'):
    main()

