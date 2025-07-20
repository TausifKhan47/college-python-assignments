
sentence = input("Enter a sentence: ")

words = sentence.split()

longest = max(words, key=len)

print("The longest word is:", longest)
