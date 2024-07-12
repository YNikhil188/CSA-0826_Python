sentence = "This is a sample sentence"
words = sentence.split()
initials = ""
for word in words:
    initials += word[0] + "."
print(initials)