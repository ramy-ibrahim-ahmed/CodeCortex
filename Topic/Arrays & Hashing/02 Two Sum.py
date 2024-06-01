def twoSum(nums, target):
    dict_ = {}
    for i, v in enumerate(nums):
        compliment = target - v
        if compliment in dict_:
            return[dict_[compliment], i]
        dict_[v] = i
    return None


# nums = [2, 7, 11, 15]
# target = 9
# print(twoSum(nums, target))

# nums = [3, 2, 4]
# target = 6
# print(twoSum(nums, target))

# nums = [3, 3]
# target = 6
# print(twoSum(nums, target))

# nums = [3, 2, 3]
# target = 6
# print(twoSum(nums, target))