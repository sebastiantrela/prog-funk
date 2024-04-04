words = ["jabłko", "banan", "pomarańcza", "truskawka", "kiwi", "kokos"]
long_words = list(filter(lambda word: len(word) > 5, words))

print(long_words)