def check_anagrams(str1, str2):
    clean_str1 = "".join(str1.split()).lower()
    clean_str2 = "".join(str2.split()).lower()
    return sorted(clean_str1) == sorted(clean_str2)

str1 = "towar"
str2 = "warto"
result = check_anagrams(str1, str2)

print(result)