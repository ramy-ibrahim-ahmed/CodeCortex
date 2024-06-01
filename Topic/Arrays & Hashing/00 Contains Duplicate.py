def containsDuplicate(nums):
    hash = set(nums)
    return True if len(hash) < len(nums) else False


def containsDuplicate(nums):
    hash = set()
    for num in nums:
        if num in hash:
            return True
        hash.add(num)
    return False


from collections import Counter


def containsDuplicate(nums):
    my_counter = Counter(nums)
    for key, value in my_counter.items():
        if value > 1:
            return True
    else:
        return False


nums = [1, 2, 3, 4]
print(containsDuplicate(nums))