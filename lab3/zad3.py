def recursive_sum(input_list):
    total_sum = 0
    for element in input_list:
        if isinstance(element, list):
            total_sum += recursive_sum(element)
        else:
            total_sum += element
    return total_sum

nested_numbers = [1, 2, [3, 4, [5, 6]], 7, [8, [9, 10]]]
total = recursive_sum(nested_numbers)

print(f"zagnieżdżona lista: {nested_numbers}")
print(f"suma wszystkich liczb zagnieżdżonych: {total}")