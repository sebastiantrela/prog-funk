def operate_on_tuple(data):
    total_sum = sum(data)
    product = 1
    for num in data:
        product *= num
    return total_sum, product

my_tuple = (1, 2, 3, 4, 5)
result = operate_on_tuple(my_tuple)

print(result)