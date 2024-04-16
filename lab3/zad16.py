def remove_whitespace(string_list):
    return [s.strip() for s in string_list]

my_strings = ["   Hello ", "   world   ","             !         "]
result = remove_whitespace(my_strings)

print(result)