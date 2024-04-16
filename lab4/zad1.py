def sum_of_even_numbers(input_list):
    return sum(item for item in input_list if item % 2 == 0)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
result = sum_of_even_numbers(numbers)

print(result)