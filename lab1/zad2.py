def make_multiplier(x):
    def multipliter(n):
        return x * n

    return multipliter


double = make_multiplier(5)

print(double(5))