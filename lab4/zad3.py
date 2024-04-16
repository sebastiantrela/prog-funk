def filter_even_values(dictionary):
    filtered_dict = {key: v for key, v in dictionary.items() if v % 2 == 0}
    return filtered_dict

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
result = filter_even_values(my_dict)

print(result)