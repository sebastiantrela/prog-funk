def sort_strings(strings):
    return sorted(strings, key = lambda x: len(x))

strings = ["jabłko", "banan", "pomarańcza", "truskawka", "kiwi", "kokos"] 
sorted_strings = sort_strings(strings)

print(sorted_strings)