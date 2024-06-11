def heightChecker(heights):
    m = len(heights)
    expected = sorted(heights)
    count = 0
    for i in range(m):
        if heights[i] != expected[i]:
            count += 1
    return count


heights = [1, 1, 4, 2, 1, 3]  # Output: 3
print(heightChecker(heights))

heights = [5, 1, 2, 3, 4]  # Output: 5
print(heightChecker(heights))

heights = [1, 2, 3, 4, 5]  # Output: 0
print(heightChecker(heights))
