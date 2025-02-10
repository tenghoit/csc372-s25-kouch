

class Cube:
    def __init__(self) -> None:
        self.faceA: list[str] = ['W' for i in range(4)]
        self.faceB: list[str] = ['B' for i in range(4)]
        self.faceC: list[str] = ['R' for i in range(4)]
        self.faceD: list[str] = ['O' for i in range(4)]
        self.faceE: list[str] = ['G' for i in range(4)]
        self.faceF: list[str] = ['Y' for i in range(4)]

    def print(self):
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
        print(f'      | {} {} |')
        print(f'      | {} {} |')
        print(f'+-----+-----+-----+')
        print(f'| {} {} | {} {} | {} {} |')
        print(f'| {} {} | {} {} | {} {} |')
        print(f'+-----+-----+-----+')
        print(f'      | {} {} |')
        print(f'      | {} {} |')
        print(f'      +-----+')
        print(f'      | {} {} |')
        print(f'      | {} {} |')
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

