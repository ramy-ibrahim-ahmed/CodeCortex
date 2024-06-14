def minIncrementForUnique(nums) -> int:
    nums.sort()
    m = len(nums)
    count_ = 0
    pointer_ = 0
    for i in range(1, m):
        if nums[i] <= nums[pointer_]:
            count_ += nums[pointer_] - nums[i] + 1
            nums[i] = nums[pointer_] + 1
        pointer_ += 1
    return count_


nums = [1, 2, 2]  # Output: 1
print(minIncrementForUnique(nums))

nums = [3, 2, 1, 2, 1, 7]  # Output: 6
print(minIncrementForUnique(nums))
