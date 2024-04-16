def custom_sort(input_list, key_func):
    return sorted(input_list, key = key_func)


my_list = ["kot", "pies", "chomik", "żółw", "świnka morska", "papuga", "mysz"]
sorted_list = custom_sort(my_list, key_func = len)  
print(sorted_list)