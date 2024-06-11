def relativeSortArray(arr1, arr2):
    hash_ = {}
    m = len(arr1)
    for i in range(m):
        if arr1[i] not in hash_.keys():
            hash_[arr1[i]] = 1
        else:
            hash_[arr1[i]] += 1
    n = len(arr2)
    result_ = []
    for i in range(n):
        result_ += [arr2[i]] * hash_[arr2[i]]
        del hash_[arr2[i]]
    remain_ = [key for key in sorted(hash_.keys())]
    o = len(remain_)
    for i in range(o):
        result_ += [remain_[i]] * hash_[remain_[i]]
    return result_


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19, 18]
arr2 = [2, 1, 4, 3, 9, 6]  # Output: [2,2,2,1,4,3,3,9,6,7,19]
print(relativeSortArray(arr1, arr2))

arr1 = [28, 6, 22, 8, 44, 17]
arr2 = [22, 28, 8, 6]
print(relativeSortArray(arr1, arr2))  # [22,28,8,6,17,44]
