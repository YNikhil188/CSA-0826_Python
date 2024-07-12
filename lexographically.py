n = int(input("Enter the value of n: "))

def countVowelStrings(n):
    return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24

result = countVowelStrings(n)
print("Number of lexicographically sorted vowel strings of length", n, ":", result)
