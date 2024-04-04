def powers_of_two():
    power = 1
    while True:
        yield power
        power *= 2

generator = powers_of_two()
for _ in range(5):
    print(next(generator))