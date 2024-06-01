def scoreOfString(s):
    result = 0
    i = 0
    m = len(s)
    while i + 1 < m:
        temp = ord(s[i]) - ord(s[i + 1])
        if temp < 0:
            temp *= -1
        result += temp
        i += 1
    return result


s = "hello"
print(scoreOfString(s))