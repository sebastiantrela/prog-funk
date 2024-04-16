def find_max_min_diff(input_list):
    if not input_list:
        return None
    
    max_val = max(input_list)
    min_val = min(input_list)
    diff = max_val - min_val
    return diff

my_list = [5, 10, 3, 8, 12, 6]
result = find_max_min_diff(my_list)

print(f"różnica między max a min wartością: {result}")  