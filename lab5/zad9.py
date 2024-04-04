from functools import reduce

number_list = [25, 65, 32, 64, 12, 56, 87, 20, 71, 44]
largest_number = reduce(lambda x, y: x if x > y else y, number_list)

print(f"Największa liczba w liście to: {largest_number}")

def average(number_list):
    total_sum = reduce(lambda x, y: x + y, number_list)
    average = total_sum / len(number_list)
    return average

result = average(number_list)
print(f"Średnia z listy liczb: {result}")
