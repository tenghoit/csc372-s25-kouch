import os
import shutil


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


def cell_to_var(row: int, col: int, letter: int) -> int:
    
    return row * 25**2 + col * 25 + letter # letter_dict[letter]


def var_to_cell(var):
    pass


def single_letter_per_cell(file):
    with open(file, 'a') as f:

        for row in range(25):
            for col in range(25):


                for first_letter in range(1, 25):

                    for second_letter in range(first_letter + 1, 26):

                        first_var = cell_to_var(row, col, first_letter)
                        second_var = cell_to_var(row, col, second_letter)

                        f.write(f'-{first_var} -{second_var} 0\n')




def single_letter_per_row(file):
    with open(file, 'a') as f:

        for letter in range(1, 26):

            for row in range(25):


                for first_col in range(24):

                    for second_col in range(first_col + 1, 25):

                        first_var = cell_to_var(row, first_col, letter)
                        second_var = cell_to_var(row, second_col, letter)

                        
                        f.write(f'-{first_var} -{second_var} 0\n')



def single_letter_per_col(file):
    
    with open(file, 'a') as f:

        for letter in range(1, 26):

            for col in range(25):


                for first_row in range(24):

                    for second_row in range(first_row + 1, 25):

                        first_var = cell_to_var(first_row, col, letter)
                        second_var = cell_to_var(second_row, col, letter)

                        
                        f.write(f'-{first_var} -{second_var} 0\n')


            
def single_letter_per_box(file):
    
    with open(file, 'a') as f:
        for letter in range(1, 26):

            for box_row in range(0, 25, 5):
                for box_col in range(0, 25, 5):


                    surrounding_cells = []

                    for row in range(5):
                        for col in range(5):
                            surrounding_cells.append([box_row + row, box_col + col])


                    for first_cell in range(24):
                        first_cell_row = surrounding_cells[first_cell][0]
                        first_cell_col = surrounding_cells[first_cell][1]

                        for second_cell in range(first_cell+1,25):
                            second_cell_row = surrounding_cells[second_cell][0]
                            second_cell_col = surrounding_cells[second_cell][1]

                            if first_cell_row == second_cell_row or first_cell_col == second_cell_col: continue

                            first_var = cell_to_var(first_cell_row, first_cell_col, letter)
                            second_var = cell_to_var(second_cell_row, second_cell_col, letter)

                            
                            f.write(f'-{first_var} -{second_var} 0\n')


def process_alpha_file(file_path, file_name):

    puzzle = []

    with open(file_path, 'r') as f:

        current_row = 0

        while current_row < 25:

            line = f.readline()
            # empty line
            if(len(line) == 1):
                continue
            #care only about letter or _
            chars = [char for char in line if char != ' ' and char != '\n']
            puzzle.append(chars)
            current_row += 1
            
            
    for row in range(len(puzzle)):
        print(f'Row {row}: {puzzle[row]}')

    # taking base cnf
    lines = []
    with open('base.cnf', 'r') as f:
        lines = f.readlines()

    additional_clauses = 0

    # scanning curr puzzle, if have letter, add unit clause
    for row in range(25):
        for col in range(25):
            if puzzle[row][col] == '_': continue

            var = cell_to_var(row, col, letter_dict[puzzle[row][col]])

            lines.append(f'{var} 0\n')
            additional_clauses += 1

    print(f'Addtional clauses: {additional_clauses}')

    # update clause cnt
    header = lines[0].split()
    header[3] = str(int(header[3]) + additional_clauses)
    lines[0] = ' '.join(header) + '\n'

    # create new cnf file
    output_directory = 'cnf'
    output_file_path = os.path.join(output_directory, file_name[:-3] + 'cnf')

    with open(output_file_path, 'w') as f:
        f.writelines(lines)

    print(f'Generated {output_file_path}')


def generate_base_cnf_file(file_path):
    single_letter_per_cell(file_path)
    single_letter_per_row(file_path)
    single_letter_per_col(file_path)
    single_letter_per_box(file_path)




def generate_puzzle_cnf_files():

    directory = 'puzzles'

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        process_alpha_file(file_path, file_name)


def read_output_file(file_path):
    vars = []

    with open(file_path, 'r') as f:
        lines = f.readlines()
        content = lines[1].split()
        content.pop()

        valid = [int(str) for str in content if str[0] != '-']

        vars = [vars[ i*25 : (i+1)*25] for i in range(24)]
        print(vars)




def main():
    # generate_base_cnf_file('base2.cnf')
    # run_experiment()

    # generate_puzzle_cnf_files()
    read_output_file()


if __name__ == '__main__':
    main()