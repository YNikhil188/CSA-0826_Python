import itertools
n=input("enter the number=")
P=list(itertools.permutations(n))
print(*[''.join(p) for p in P])