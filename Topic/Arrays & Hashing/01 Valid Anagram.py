def isAnagram(s, t):
    if len(s) != len(t):
        return False
    a = sorted(s)
    b = sorted(t)
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def isAnagram(s, t):
    m1 = len(s)
    m2 = len(t)
    if m1 == m2 and m1 == 1 and s[0] != t[0]:
        return False
    if m1 != m2:
        return False
    dict_ = dict()
    counter1 = 0
    counter2 = 0
    for i in range(m1):
        if i == m1 - 1 and s[i] == t[i]:
            continue
        if dict_.get(s[i], 0) == 0:
            dict_[s[i]] = 1
        else:
            counter1 += 1
        if dict_.get(t[i], 0) == 0:
            dict_[t[i]] = 1
        else:
            counter2 += 1
    return True if counter1 == counter2 else False


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))

s = "rat"
t = "car"
print(isAnagram(s, t))
