def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = generate_fibonacci()
first_10 = [next(fib_gen) for _ in range(10)]

print(f"pierwsze 10 liczb ciągu Fibonacciego: {first_10}")