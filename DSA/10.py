def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

string = input("Enter a string: ")
length = string_length(string)
print("Length of the string is:", length)
