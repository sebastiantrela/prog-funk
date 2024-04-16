def filter_long_words(word_list):
    avg_len = sum(len(word) for word in word_list) / len(word_list)
    print(f"średnia długość wszystkich stringów w liście: {avg_len}")

    long_words = [word for word in word_list if len(word) > avg_len]
    return long_words

words = ["kot", "pies", "chomik", "żółw", "świnka morska", "papuga", "mysz"]
filtered_words = filter_long_words(words)

print(f"stringi dłuższe niż średnia długość wszsytkich stringów: {filtered_words}")
