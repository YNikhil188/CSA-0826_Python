def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] in s[:i] or t[i] in t[:i]:
                return False

    return True
s = "egg"
t = "add"
print(is_isomorphic(s, t))
s = "foo"
t = "bar"
print(is_isomorphic(s, t)) 