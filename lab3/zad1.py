def double_list_elements(input_list):
    doubled_list = [element * 2 for element in input_list]
    return doubled_list

numbers = [1, 2, 3, 4, 5]
doubled_numbers = double_list_elements(numbers)

print(doubled_numbers)