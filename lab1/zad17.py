from functools import partial

def add(x, y):
    return x + y

just_add = partial(add, 5)
result = just_add(15)

print(result)