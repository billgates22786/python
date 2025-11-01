def reverse_sentence(sentence):
    if len(sentence) == 0:
        return sentence
    return reverse_sentence(sentence[1:]) + sentence[0]
s = input("Enter a sentence: ")
print("Reversed sentence:", reverse_sentence(s))
