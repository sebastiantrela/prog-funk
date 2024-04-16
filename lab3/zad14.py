def count_unique_elements(input_list):
    unique_elements = set(input_list)
    return len(unique_elements)

my_list = [1, 2, 3, 4, 5, 6, 6, 2, 3]
count = count_unique_elements(my_list)

print(f"liczba unikalnych elementów: {count}")