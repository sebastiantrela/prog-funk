def cumulative_sum(input_list):
    cumulative = []
    total = 0
    for element in input_list:
        total += element
        cumulative.append(total)
    return cumulative

my_list = [1, 2, 3, 4, 5]
result = cumulative_sum(my_list)

print(f"suma skumulowana: {result}")