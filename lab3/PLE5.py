
sentence = input("Enter a sentence: ")

words = sentence.strip().split()

if words:
    last_word = words[-1]
    print("The last word is:", last_word)
    print("Length of the last word:", len(last_word))
else:
    print("The sentence is empty or has no words.")
