# i need to take O(1) place so i need to modify s
# reverse the order without creating a new list
def reverseString(s):
    m = len(s)
    for i in range(m // 2):
        last_index = m - i - 1
        TMP = s[i]
        s[i] = s[last_index]
        s[last_index] = TMP
    return s


s = ["h", "e", "l", "l", "o"]  # Output: ["o","l","l","e","h"]
print(reverseString(s))

s = ["H", "a", "n", "n", "a", "h"]  # Output: ["h","a","n","n","a","H"]
print(reverseString(s))