def flatten_list(nested_list):
    flattened = []
    for element in nested_list:
        if isinstance(element, list):
            flattened.extend(flatten_list(element))
        else:
            flattened.append(element)
    return flattened

nested_list = [1, [2, 3], [4, [5, 6], 7], 8, [9, 10]]
flattened_result = flatten_list(nested_list)

print(f"lista przed użyciem funkcji: {nested_list}")
print(f"lista po użyciu funkcji: {flattened_result}")