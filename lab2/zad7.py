from itertools import groupby

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Creating groups based on evenness
even_numbers = []
odd_numbers = []
for k, g in groupby(numbers, key = lambda x: x % 2 == 0):
    if k:
        even_numbers.extend(g)
    else:
        odd_numbers.extend(g)

# Displaying groups with appropriate labels
print(f"parzyste: {even_numbers}")
print(f"nieparzyste: {odd_numbers}")
