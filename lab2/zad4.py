numbers = [2, 3, 8, 12, 5, 16, 7]
squares = [x**2 for x in numbers if (square := x**2) > 10]

print(f"lista kwadratów liczb większych od 10: {squares}")