def split_list(input_list, chunk_size):
    split_lists = []
    for i in range(0, len(input_list), chunk_size):
        split_lists.append(input_list[i: i + chunk_size])
    return split_lists

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunks = split_list(my_list, 3)

print(f"podzielona lista: {chunks}") 