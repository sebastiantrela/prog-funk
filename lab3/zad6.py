def map_nested(nested_list, func):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.append(map_nested(item, func))
        else:
            result.append(func(item))
    return result

nested_list = [1, 2, [3, 4], [5, [6, 7]], 7, 8, [9, 10]]
mapped_list = map_nested(nested_list, lambda x: x * 2)

print(f"zagnieżdzona lista: {nested_list}")
print(f"lista po zastosowaniu funkcji: {mapped_list}")