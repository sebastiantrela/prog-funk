from collections import Counter

def most_common_element(input_list):
    counts = Counter(input_list)
    return max(counts, key = counts.get)

my_list = [1, 2, 3, 2, 2, 4, 5, 2, 3]
result = most_common_element(my_list)
print(result)