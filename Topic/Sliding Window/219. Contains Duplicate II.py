### HASH MAP ###
def containsNearbyDuplicate(nums, k):
    num_indices = {}
    
    for i, num in enumerate(nums):
        if num in num_indices and abs(i - num_indices[num]) <= k:
            return True
        num_indices[num] = i
    
    return False

### SLIDING SHOW ###
def containsNearbyDuplicate(nums, k):
    num_set = set()
    
    for i in range(len(nums)):
        if nums[i] in num_set:
            return True
        num_set.add(nums[i])
        if len(num_set) > k:
            num_set.remove(nums[i - k])
    
    return False


### TEST CASE ###
nums, k = [1, 0, 1, 1], 1  # Output: true
print(containsNearbyDuplicate(nums, k))


nums, k = [1, 2, 3, 1, 2, 3], 2  # Output: false
print(containsNearbyDuplicate(nums, k))
