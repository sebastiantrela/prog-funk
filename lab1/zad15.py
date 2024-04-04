def add(x):
    def inner(y):
        return x + y
    return inner

just_add = add(9)
result = just_add(10)

print(result)