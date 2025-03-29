import os
import sys
import time
import random


class SAT:

    def __init__(self, file_name: str):
        self.num_variables: int = 0
        self.num_clauses: int = 0
        self.clauses: list[list[int]] = []

        self.process_cnf_file(file_name)

    def process_cnf_file(self, file_name: str):

        with open(file_name, 'r') as file:

            line = file.readline()
            while line[0] == 'c':
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
    

    def get_false_clauses(self, assignment: list[int]):

        result = []

        for disjunction in self.clauses:

            valid = False

            for literal in disjunction:

                if literal == assignment[abs(literal)]:
                    valid = True
                    break

            if valid == False:
                result.append(disjunction)


        return result




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

    
    def walkSAT(self, probability: float, max_flips: int):

        # inital random
        assignment = [i if random.random() < 0.5 else -i for i in range(self.num_variables + 1)]

        
        for iteration in range(max_flips):
            print(f'\nIteration {iteration}')
            print(f'Starting Assignment: {assignment} | Score: {self.evaluate_assignment(assignment)}')

            if self.is_SAT(assignment) == True:
                print(f'SAT: {assignment}')
                return
            

            false_clauses = self.get_false_clauses(assignment)

            selected_clause = random.choice(false_clauses)
            print(f'Selected Clause: {selected_clause}')

            if random.random() < probability: 
                
                selected_literal = random.choice(selected_clause)

                assignment[abs(selected_literal)] *= -1

                print(f'Random Walk: {assignment[abs(selected_literal)]}')

            else:
                best_assignment = []
                best_score = float('-inf')

                for literal in selected_clause:
                    print(literal)

                    new_assignment = assignment[:]
                    print(new_assignment)

                    new_assignment[abs(literal)] *= -1

                    new_score = self.evaluate_assignment(new_assignment)

                    print(f'New assignment: {new_assignment} | New score: {new_score}')

                    if new_score > best_score:
                        best_assignment = new_assignment
                        best_score = new_score
                        print(f'Best Assignment: {new_assignment} | Score: {new_score}')

                assignment = best_assignment

        
        return None


def main():
    
    if len(sys.argv) != 2:
        print(f'Usage {sys.argv[0]} <filename.cnf>')
        exit()

    axo = SAT(sys.argv[1])
    axo.walkSAT(0.5, 1000000)
    


if __name__ ==  '__main__':
    main()