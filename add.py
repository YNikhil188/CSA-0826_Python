string="apple"
vowels='aeiou'
vowel_count=0
for char in string:
    if char in vowels:
        vowel_count+=1
print(f"the string '{string}' contains {vowel_count} vowels in it")
