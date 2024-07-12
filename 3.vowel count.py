statement="saveetha school of engineering"
statement=statement.lower()
vowel_count=0
vowels='a','e','i' , 'o', 'u'
for char in statement:
      if char in vowels:
            vowel_count=vowel_count+1
print("Number of vowels in the given sentence is :",vowel_count)