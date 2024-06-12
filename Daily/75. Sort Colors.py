def sortColors(nums):
    hash_ = {0: 0, 1: 0, 2: 0}
    m = len(nums)
    result_ = []
    for i in range(m):
        hash_[nums[i]] += 1
    for i in range(3):
        result_ += [i] * hash_[i]
    return result_


def sortColors(nums):
    pointer_ = 0
    m = len(nums)
    for i in range(m):
        if nums[pointer_] == 2:
            del nums[pointer_]
            nums.append(2)
        elif nums[pointer_] == 0:
            del nums[pointer_]
            nums.insert(0, 0)
            pointer_ += 1
        else:
            pointer_ += 1
    return nums


nums = [2, 0, 2, 1, 1, 0]  # Output: [0,0,1,1,2,2]
print(sortColors(nums))

nums = [2, 0, 1]  # Output: [0,1,2]
print(sortColors(nums))
