import heapq
from collections import Counter


def topKFrequent(nums, k):
    frequent = Counter(nums)
    ordered_keys = list(key for key, _ in frequent.most_common())[:k]
    return ordered_keys


def topKFrequent(nums, k):
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    min_heap = []
    for num, freq in freq_dict.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return [v[1] for v in min_heap]


nums = [4, 1, -1, 2, -1, 2, 3]
k = 2
print(topKFrequent(nums, k))