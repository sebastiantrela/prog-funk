from itertools import combinations

def generate_combinations(elements):
    combinations_list = list(combinations(elements, 2))
    return  combinations_list

elements_list = [1, 2, 3, 4]
combinations_result = generate_combinations(elements_list)

print(f"wszystkie możwlie 2-elementwoe kombinacje: {combinations_result}")