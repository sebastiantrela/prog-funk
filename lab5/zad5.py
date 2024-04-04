def even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

area = lambda a, b: a * b

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Liczby parzyste: ", even_numbers(numbers))

a, b = 3, 15
print("Pole prostokąta: ", area(a, b))
