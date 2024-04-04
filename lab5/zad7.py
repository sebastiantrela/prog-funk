def square(x):
    return x**2

def add(x):
    return x + 5

def composition(f1, f2):
    return lambda x: f1(f2(x))

numbers = [1, 2, 3, 4, 5]

result = list(map(composition(square, add), numbers))
print(f"wynik: {result}")

def apply(list_of_functions, value):
    result = value
    for function in list_of_functions:
        result = function(result)
    return result

def multiplication(x):
    return x * 3

def addition(x):
    return x + 2

def subtraction(x):
    return x - 1

list_of_functions = [multiplication, addition, subtraction]
value = 10
result = apply(list_of_functions, value)
print(f"wynik: {result}")
