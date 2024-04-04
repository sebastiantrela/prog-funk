from functools import reduce

numbers = [5, 6, 7, 8, 9, 10]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print(f"Suma liczb z listy to: {sum_of_numbers}")