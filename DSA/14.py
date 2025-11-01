def remove_repeated_words(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if word not in result:
            result.append(word)
    return ' '.join(result)
sentence = input("Enter a string: ")
print("String after removing repeated words:")
print(remove_repeated_words(sentence))
