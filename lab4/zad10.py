from itertools import permutations

def generate_permutation(input_list):
    return list(permutations(input_list))

my_list = [1, 2, 3]
result = generate_permutation(my_list)

print(result)