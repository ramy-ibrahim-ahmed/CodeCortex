def groupAnagrams(strs):
    str_dict = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        str_dict.setdefault(sorted_word, []).append(word)
    return str_dict


# def groupAnagrams(strs):
#     dict_ = {}
#     for word in strs:
#         total = 0
#         for char in word:
#             total += ord(char)
#         if total in dict_:
#             dict_[total].append(word)
#         else:
#             dict_[total] = [word]
#     return list(dict_.values())

from collections import defaultdict


def groupAnagrams(strs):
    MAP = defaultdict(list)
    for word in strs:
        sorted_word = "".join(sorted(word))
        MAP[sorted_word].append(word)
    return list(MAP.values())


# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(groupAnagrams(strs))

# strs = [""]
# print(groupAnagrams(strs))

# strs = ["a"]
# print(groupAnagrams(strs))
