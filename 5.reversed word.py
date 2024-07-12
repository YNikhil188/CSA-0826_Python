word=str(input("enter the word:"))
reversed_word=""
for char in word[::-1]:
    reversed_word+=char
print("the reversed word is",reversed_word)
