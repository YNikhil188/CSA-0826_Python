word = input("Enter a word: ")
sorted_word = "".join(sorted(word.lower(), reverse=True))
print("Alphabetically arranged word in reverse order:", sorted_word)