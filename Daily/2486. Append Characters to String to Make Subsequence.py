# two pointers for tracking each string and they move independently
def appendCharacters(s, t):
    m = len(s)
    n = len(t)
    S = 0
    T = 0
    while T < n and S < m:
        if s[S] == t[T]:
            T += 1
        S += 1
    return n - T


s, t = "coaching", "coding"  # Output: 4
print(appendCharacters(s, t))

s, t = "abcde", "a"  # Output: 0
print(appendCharacters(s, t))

s, t = "z", "abcde"  # Output: 5
print(appendCharacters(s, t))

s, t = "lbg", "g"  # Output: 0
print(appendCharacters(s, t))
