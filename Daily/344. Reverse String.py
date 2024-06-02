# i need to take O(1) place so i need to modify s
# reverse the order without creating a new list
def reverseString(s):
    left = None
    right = None
    for i in range(len(s) // 2):
        last_index = len(s) - i - 1
        left = s[i]
        right = s[last_index]
        s[last_index] = left
        s[i] = right
    return s


s = ["h", "e", "l", "l", "o"]  # Output: ["o","l","l","e","h"]
print(reverseString(s))

s = ["H", "a", "n", "n", "a", "h"]  # Output: ["h","a","n","n","a","H"]
print(reverseString(s))