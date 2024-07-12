word=input("enter the word:")
reversed_word=""
for i in range (len(word) -1,-1,-1):
    reversed_word+=word[i]
print("reversed word is:",reversed_word)