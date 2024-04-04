def compose(f, g):
    def composed_function(x):
        return f(g(x))
    return composed_function

def add_one(x):
    return x + 1

def multiply(x):
    return x * 2

composed_function = compose(add_one, multiply)
result = composed_function(7)

print(result)