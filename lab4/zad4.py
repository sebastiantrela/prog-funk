def power_function(exponent):
    return lambda x: x**exponent

square = power_function(2)
result = square(5)

print(result)