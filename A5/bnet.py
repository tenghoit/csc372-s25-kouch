import sys


class Node:
    def __init__(self, cpt, parents=None):
        self.cpt = cpt
        self.parents = parents

    def get_probability(self, val, assignment):

        if self.parents is None:
            p_true = self.cpt[()]
        else:
            parent_values = tuple(assignment[parent] for parent in self.parents)
            p_true = self.cpt[(parent_values)]

        return p_true if val == True else (1 - p_true) # else is for p_false 



class BayesNet:
    def __init__(self):
        self.nodes = {
            'E': Node({(): 0.03}),

            'B': Node({(): 0.02}),

            'A': Node({
                (True, True): 0.97,
                (True, False): 0.92,
                (False, True): 0.36,
                (False, False): 0.03
            }, ['B', 'E']),

            'J': Node({
                (True): 0.85,
                (False): 0.07
            }, ['A']),

            'M': Node({
                (True): 0.69,
                (False): 0.02
            }, ['A'])
        }


    def full_joint_distribution(self, assignment, given):

        products = []

        for var in assignment.keys():
            
            probability = self.nodes[var].get_probability(assignment[var], assignment)

            products.append(probability)


        result = 1
        for probability in products:
            result *= probability


        return result





def process_query(query: list[str], assignment, given):
    truth = {'t': True, 'f': False}

    query.pop(0) #get rid of program_name

    if 'given' in query:    
        given_index = query.index('given')
        given_query = query[given_index + 1:]

        for str in given_query:
            given[str[0]] = truth[str[1]]

        query = query[:given_index]

    
    for str in query:
        assignment[str[0]] = truth[str[1]]



def main():

    if len(sys.argv) < 2 or len(sys.argv) > 7:
        exit('Invalid Usage: bnet.py arg1 [arg2 ... arg6]')

    print(sys.argv)

    assignment = {}
    given = {}

    process_query(sys.argv, assignment, given)

    BN = BayesNet()
    result = BN.full_joint_distribution(assignment, given)

    print(f'Assignment: {assignment} | Given: {given} | Result: {result}')

if __name__ == '__main__':
    main()