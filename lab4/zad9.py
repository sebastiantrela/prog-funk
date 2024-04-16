def apply_function_to_tuples(input_tuples, func):
    return [func(*t) for t in input_tuples]

def add(x, y):
    return x + y

my_tuples = [(1, 2), (3, 4), (5, 6)]
result = apply_function_to_tuples(my_tuples, add)
print(result)