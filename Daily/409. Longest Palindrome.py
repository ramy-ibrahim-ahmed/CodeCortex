def longestPalindrome(s):
    m = len(s)
    EVEN = 0
    FLAG = 0
    ODD = []
    for c in range(m):
        if s[c] in ODD:
            ODD.remove(s[c])
            EVEN += 2
            # FLAG += 1
        else:
            ODD.append(s[c])
    return EVEN if len(ODD) == 0 else EVEN + 1
    # return EVEN if FLAG == m / 2 else EVEN + 1


s1 = "abccccdd"  # Output: 7
print(longestPalindrome(s1))

s = "a"  # Output: 1
print(longestPalindrome(s))

########################################################################################


import cProfile
import timeit

# cProfile.run("longestPalindrome(s)")
elapsed_time = timeit.timeit(lambda: longestPalindrome(s1), number=1000)
print(f"Execution time: {elapsed_time:.6f} seconds")
