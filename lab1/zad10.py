even_numbers_generator = (x for x in range(0, 2**31, 2))

for _ in range(10): # można zmienić ile się chce wyświetlić
    print(next(even_numbers_generator))