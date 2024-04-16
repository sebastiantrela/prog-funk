def rotate_list(input_list, steps):
    if not input_list:
        return []
    steps = steps % len(input_list)
    return input_list[-steps:] + input_list[:-steps]

my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(my_list, 2)

print("obrócona lista:", rotated_list)