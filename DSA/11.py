def concatenate_strings(s1, s2):
    return s1 + s2
def compare_strings(s1, s2):
    if s1 == s2:
        return "Strings are equal"
    else:
        return "Strings are not equal"
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
concatenated = concatenate_strings(str1, str2)
print("Concatenated string:", concatenated)
print(compare_strings(str1, str2))
