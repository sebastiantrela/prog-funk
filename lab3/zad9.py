def zip_with_index(lst):
    return list(enumerate(lst))

my_list = ["a", "b", "c", "d"]
indexed_list = zip_with_index(my_list)

print(f"lista z indeksami: {indexed_list}")