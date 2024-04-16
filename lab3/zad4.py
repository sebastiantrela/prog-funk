def remove_duplicates(input_list):
    seen = {}
    unique_list = []

    for element in input_list:
        if element not in seen:
            unique_list.append(element)
            seen[element] = True
    return unique_list

duplicated_list = [1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 7]
unique_elements = remove_duplicates(duplicated_list)

print(f"oryginalna lista: {duplicated_list}")
print(f"lista bez duplikatów: {unique_elements}")