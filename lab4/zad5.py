def chunk(input_list, size):
    return [input_list[i: i + size] for i in range(0, len(input_list), size)]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = chunk(my_list, 5)

print(result)