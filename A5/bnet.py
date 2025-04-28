import sys
import random


class Node:
    def __init__(self, cpt, parents=None):
        self.cpt = cpt
        self.parents = parents

    def get_probability(self, val: bool, assignment):

        if self.parents is None:
            p_true = self.cpt[()]
        else:
            key = tuple(assignment[parent] for parent in self.parents)
            p_true = self.cpt[key]

        return p_true if val == True else (1 - p_true) # else is for p_false 



class BayesNet:
    def __init__(self, query=None):
        self.nodes = {
            'B': Node({(): 0.02}),

            'E': Node({(): 0.03}),

            'A': Node({
                (True, True): 0.97,
                (True, False): 0.92,
                (False, True): 0.36,
                (False, False): 0.03
            }, ['B', 'E']),

            'J': Node({
                (True,): 0.85,
                (False,): 0.07
            }, ['A']),

            'M': Node({
                (True,): 0.69,
                (False,): 0.02
            }, ['A'])
        }

        self.assignment = {}
        self.given = {}

        if query is not None: self.read_query(query)


    def read_query(self, query):
        truth = {'t': True, 'f': False}
        query.pop(0) #get rid of program_name

        if 'given' in query:    
            given_index = query.index('given')
            given_query = query[given_index + 1:]

            for str in given_query:
                self.given[str[0]] = truth[str[1]]

            query = query[:given_index]
        
        for str in query:
            self.assignment[str[0]] = truth[str[1]]


    def __str__(self):
        return f'Nodes: {self.nodes}\nAssignment: {self.assignment}\nGiven: {self.given}'
    
    def build_full_joint_distribution_table(self):
        # build table
        table = {}
        for i in range(32):
            binary_num = bin(i)[2:].zfill(len(self.nodes))

            current_key = tuple(True if char == '1' else False for char in binary_num)

            current_assignment = {}
            for index, node in enumerate(self.nodes.keys()):
                current_assignment[node] = current_key[index]

            # print(current_assignment)

            probabilty = 1.0
            for key, val in current_assignment.items():
                probabilty *= self.nodes[key].get_probability(val, current_assignment)
            # print(probabilty)

            table[current_key] = probabilty

        return table


    def full_joint_distribution(self):

        full_joint_distribution_table = self.build_full_joint_distribution_table()

        true_assignment_probability = 0
        true_given_probability = 0
        
        for key, val in full_joint_distribution_table.items():

            current_assignment = {}
            for index, node in enumerate(self.nodes.keys()):
                current_assignment[node] = key[index]

            # print(current_assignment)

            # check if matches given
            match_given_evidence = all(current_assignment.get(node) == self.given.get(node) for node in self.given)
            if match_given_evidence:
                true_given_probability += val
                
                # check if matches assignment
                match_assignment = all(current_assignment.get(node) == self.assignment.get(node) for node in self.assignment)
                if match_assignment:
                    true_assignment_probability += val


        # print(f'True %: {true_assignment_probability}\nGiven %: {true_given_probability}')
        return true_assignment_probability/true_given_probability

    
    def generate_sample(self):

        new_assignment = {}

        for key, node in self.nodes.items():

            threshold = node.get_probability(True, new_assignment)

            if random.random() < threshold:
                new_assignment[key] = True
            else:
                new_assignment[key] = False

        return new_assignment
    

    def rejection_sampling(self, num_iterations):

        true_assignment_count = 0
        true_given_count = 0

        for iteration in range(num_iterations):
            # print(f'Iteration {iteration}: Assignment #: {true_assignment_count} | Given #: {true_given_count}')
            
            new_sample = self.generate_sample()

            # check if matches given
            match_given_evidence = all(new_sample.get(node) == self.given.get(node) for node in self.given)
            if match_given_evidence:
                true_given_count += 1
                
                # check if matches assignment
                match_assignment = all(new_sample.get(node) == self.assignment.get(node) for node in self.assignment)
                if match_assignment:
                    true_assignment_count += 1

        return (true_assignment_count/true_given_count) if true_given_count != 0 else 0





def main():

    # if len(sys.argv) < 2 or len(sys.argv) > 7:
    #     exit('Invalid Usage: bnet.py arg1 [arg2 ... arg6]')

    queries = [
        ['bnet', 'Bt', 'Af', 'given', 'Mf'], 
        ['bnet', 'Af', 'Et'],
        ['bnet', 'Jt', 'Af', 'given', 'Bt', 'Ef'],
        ['bnet', 'Bt', 'Af', 'Mf', 'Jt', 'Et']
    ]

    for query in queries:
        print(query)
        BN = BayesNet(query)
        print(f'    FJD: {BN.full_joint_distribution()}')
        # print(BN.generate_sample())
        rs_results = []
        for i in range(10):
            rs_results.append(BN.rejection_sampling(10000000))
        rs_avg = sum(rs_results)/len(rs_results)
        print(f'    RS: {rs_avg}')
    

if __name__ == '__main__':
    main()