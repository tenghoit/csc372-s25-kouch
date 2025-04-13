import os

def cell_to_var(row: int, col: int, letter: int) -> int:
    
    letter_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25
    }

    return row * 25**2 + col * 25 + letter # letter_dict[letter]


def single_letter_per_cell(file):

    for row in range(25):
        for col in range(25):


            for first_letter in range(1, 25):

                for second_letter in range(first_letter + 1, 26):

                    first_var = cell_to_var(row, col, first_letter)
                    second_var = cell_to_var(row, col, second_letter)

                    with open(file, 'a') as f:
                        f.write(f'-{first_var} -{second_var} 0')




def single_letter_per_row(file):

    for letter in range(1, 26):

        for row in range(25):


            for first_col in range(24):

                for second_col in range(first_col + 1, 25):

                    first_var = cell_to_var(row, first_col, letter)
                    second_var = cell_to_var(row, second_col, letter)

                    with open(file, 'a') as f:
                        f.write(f'-{first_var} -{second_var} 0')



def single_letter_per_col(file):

    for letter in range(1, 26):

        for col in range(25):


            for first_row in range(24):

                for second_row in range(first_row + 1, 25):

                    first_var = cell_to_var(first_row, col, letter)
                    second_var = cell_to_var(second_row, col, letter)

                    with open(file, 'a') as f:
                        f.write(f'-{first_var} -{second_var} 0')


            
def single_letter_per_box(file):

    for letter in range(1, 26):

        for box_row in range(0, 25, 5):
            for box_col in range(0, 25, 5):


                surrounding_cells = []

                for row in range(5):
                    for col in range(5):
                        surrounding_cells.append([box_row + row, box_col + col])


                for first_cell in range(24):
                    for second_cell in range(first_cell+1,25):

                        first_var = cell_to_var(surrounding_cells[first_cell][0], surrounding_cells[first_cell][1], letter)
                        second_var = cell_to_var(surrounding_cells[second_cell][0], surrounding_cells[second_cell][1], letter)

                        with open(file, 'a') as f:
                            f.write(f'-{first_var} -{second_var} 0')


def parse_alpha_file(file):

    with open(file, 'r') as f:
        line = f.readline()

        chars = [char for char in line if char != ' ']
        print(chars)





def main():
    parse_alpha_file('puzzles/alpha_0.txt')


if __name__ == '__main__':
    main()