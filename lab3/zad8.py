def partition_list(input_list, condition):
    true_list = []
    false_list = []
    for element in input_list:
        if condition(element):
            true_list.append(element)
        else:
            false_list.append(element)

    return true_list, false_list

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
true_numbers, false_numbers = partition_list(numbers, is_even)

print(f"elementy spełniające warunek: {true_numbers}")
print(f"pozostałe elementy: {false_numbers}")