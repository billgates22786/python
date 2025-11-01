sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Sort words alphabetically (case-insensitive)
words.sort(key=str.lower)

print("Words in alphabetical order:")
for word in words:
    print(word)
