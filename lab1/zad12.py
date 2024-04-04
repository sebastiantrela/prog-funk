from functools import partial

def multiply(x, y):
    return x * y

multiply3 = partial(multiply, y = 3)
result = multiply3(12)

print(result)