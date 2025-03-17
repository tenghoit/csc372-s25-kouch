import os
import sys
import time


class SAT:

    def __init__(self, file_name: str):
        self.num_variables: int = 0
        self.num_clauses: int = 0
        self.clauses: list[list[int]] = []

        self.process_cnf_file(file_name)

    def process_cnf_file(self, file_name: str):

        with open(file_name, 'r') as file:

            line = file.readline()

            if(line != ''):
                metadata = line.split()
                self.num_variables = int(metadata[2])
                self.num_clauses = int(metadata[3])

                print(f'# Vars: {self.num_variables} | # clauses: {self.num_clauses}')
            else:
                exit("Error processing file.")

            for row in range(self.num_clauses):
                line = file.readline()

                new_clause = line.split()
                new_clause = [ int(new_clause[i]) for i in range(0, len(new_clause) - 1)]
                self.clauses.append(new_clause)

        print(self.clauses)


    def evaluate_assignment(self, assignment: list[int]):
        result = 0

        for disjunction in self.clauses:

            for literal in disjunction:

                if literal == assignment[abs(literal)]:
                    result += 1
                    break

        return result


    def is_SAT(self, assignment: list[int]):

        for disjunction in self.clauses:

            valid = False

            for literal in disjunction:

                if literal == assignment[abs(literal)]:
                    valid = True
                    break

            if valid == False:
                return False
            
        return True


    def hill_climb(self):
        
        assignment = [i for i in range(self.num_variables + 1)]
        score = self.evaluate_assignment(assignment)

        iteration = 0
        while(self.is_SAT(assignment) == False):
            print(f'\nIteration {iteration}')
            print(f'Starting Assignment: {assignment} | Score: {score}')

            best_assignment = assignment
            best_score = score

            for i in range(1, len(assignment)):
                new_assignment = assignment[:]
                new_assignment[i] *= -1

                new_score = self.evaluate_assignment(new_assignment)
                print(f'New assignment: {new_assignment} | New score: {new_score}')

                if new_score > best_score:
                    best_score = new_score
                    best_assignment = new_assignment
                    print(f'Best Assignment: {new_assignment} | Score: {new_score}')

            assignment = best_assignment
            iteration += 1

        print(f'SAT: {assignment}')

    



def DPLL(clauses: list[list[int]]):
    pass



def walkSAT(clauses: list[list[int]]):
    pass



def main():
    
    if len(sys.argv) != 2:
        print(f'Usage {sys.argv[0]} <filename.cnf>')
        exit()

    axo = SAT(sys.argv[1])
    axo.hill_climb()
    


if __name__ ==  '__main__':
    main()