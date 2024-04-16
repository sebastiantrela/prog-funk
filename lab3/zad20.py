def sum_of_squares_of_odds(input_list):
    return sum(x**2 for x in input_list if x % 2 != 0)

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_squares_of_odds(my_numbers)

print(f"suma kwadratów liczb nieparzystych: {result}")