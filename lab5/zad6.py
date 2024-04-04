words_list = ["jabłko", "ananas", "pomarańcza", "arbuz", "nektarynka", "awokado"]
words = list(filter(lambda slowo: slowo.startswith('a'), words_list))

print(f"słowa zaczynające się na 'a': {words}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x**2, numbers))

print(f"lista liczb: {numbers}")
print(f"lista kwadratów: {squares}")