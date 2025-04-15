import os
import sys
from pysat.solvers import Minisat22


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

int_to_letter = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P',
    17: 'Q',
    18: 'R',
    19: 'S',
    20: 'T',
    21: 'U',
    22: 'V',
    23: 'W',
    24: 'X',
    25: 'Y'
}

def cell_to_var(row: int, col: int, letter: int) -> int:    
    return row * 25**2 + col * 25 + letter 

def var_to_cell(var):
    var -= 1  # shift to 0-based index if your encoding started at 1

    row = var // 625
    var %= 625

    col = var // 25
    var %= 25

    letter = var + 1  # letters are from 1 to 25

    return [row, col, int_to_letter[letter]]


def var_to_letter(var):
    remainder = var % 25
    if remainder == 0:
        remainder = 25

    return int_to_letter[remainder]


def at_least_one_letter_in_each_cell(solver):
    for row in range(25):
        for col in range(25):
            
            clause = []

            for letter in range(1, 26):
                var = cell_to_var(row, col, letter)
                clause.append(var)
            
            solver.add_clause(clause)


def at_least_one_letter_in_each_row(solver):
    for letter in range(1, 26):

        for row in range(25):

            clause = []

            for col in range(25):
                var = cell_to_var(row, col, letter)
                clause.append(var)

            solver.add_clause(clause)


def at_least_one_letter_in_each_col(solver):
    for letter in range(1, 26):

        for col in range(25):

            clause = []

            for row in range(25):
                var = cell_to_var(row, col, letter)
                clause.append(var)

            solver.add_clause(clause)


def at_least_one_letter_in_each_box(solver):
    for letter in range(1, 26):

        for box_row in range(0, 25, 5):
            for box_col in range(0, 25, 5):

                surrounding_cells = []

                for row in range(5):
                    for col in range(5):
                        surrounding_cells.append([box_row + row, box_col + col])

                clause = []

                for cell in surrounding_cells:

                    var = cell_to_var(cell[0], cell[1], letter)
                    clause.append(var)

                solver.add_clause(clause)


def at_most_one_letter_in_each_cell(solver):
    for row in range(25):
        for col in range(25):

            for first_letter in range(1, 25):

                for second_letter in range(first_letter + 1, 26):

                    first_var = cell_to_var(row, col, first_letter)
                    second_var = cell_to_var(row, col, second_letter)

                    solver.add_clause([-(first_var), -(second_var)])


def at_most_one_letter_in_each_row(solver):
    for letter in range(1, 26):
        for row in range(25):

            for first_col in range(24):
                for second_col in range(first_col + 1, 25):

                    first_var = cell_to_var(row, first_col, letter)
                    second_var = cell_to_var(row, second_col, letter)
                    
                    solver.add_clause([-(first_var), -(second_var)])


def at_most_one_letter_in_each_col(solver):
    for letter in range(1, 26):
        for col in range(25):

            for first_row in range(24):
                for second_row in range(first_row + 1, 25):

                    first_var = cell_to_var(first_row, col, letter)
                    second_var = cell_to_var(second_row, col, letter)
                    
                    solver.add_clause([-(first_var), -(second_var)])


def at_most_one_letter_in_each_box(solver):
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

                        
                        solver.add_clause([-(first_var), -(second_var)])



def build_base_clauses(solver):
    at_least_one_letter_in_each_cell(solver)
    at_least_one_letter_in_each_row(solver)
    at_least_one_letter_in_each_col(solver)
    at_least_one_letter_in_each_box(solver)

    at_most_one_letter_in_each_cell(solver)
    at_most_one_letter_in_each_row(solver)
    at_most_one_letter_in_each_col(solver)
    at_most_one_letter_in_each_box(solver)


def process_alpha_file(solver, file_path):

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


    # scanning curr puzzle, if have letter, add unit clause
    for row in range(25):
        for col in range(25):
            if puzzle[row][col] == '_': continue

            var = cell_to_var(row, col, letter_dict[puzzle[row][col]])

            solver.add_clause([var])


def print_model(model, output=sys.stdout):
    position = 0
    for var in model:
        if var < 0:
            continue
        letter = var_to_letter(var)
        print(f'{letter} ', end='', file=output)
        position += 1
        if position % 5 == 0:
            print(' ', end='', file=output)
        if position % 25 == 0:
            print(file=output)
        if position % 125 == 0:
            print(file=output)

def is_unique(solver, output=sys.stdout):
    model = solver.get_model()
    assignment = [-var for var in model if var > 0]
    solver.add_clause(assignment)

    if solver.solve():
        print("Additional Solution", file=output)
        model = solver.get_model()
        print_model(model, output)
    else:
        print("Solution is unique", file=output)

def solve_puzzle(file_path, output=sys.stdout):
    solver = Minisat22()
    build_base_clauses(solver)
    process_alpha_file(solver, file_path)

    if solver.solve():
        print("SATISFIABLE", file=output)
        model = solver.get_model()
        print_model(model, output)
        is_unique(solver, output)
    else:
        print("No Solution", file=output)



def main():
    dir = 'puzzles'
    with open('log.txt', 'w') as log:
        for file_name in os.listdir(dir):
            file_path = os.path.join(dir, file_name)
            print(file_name)
            print(file_name, file=log)
            solve_puzzle(file_path, output=log)






if __name__ == '__main__':
    main()