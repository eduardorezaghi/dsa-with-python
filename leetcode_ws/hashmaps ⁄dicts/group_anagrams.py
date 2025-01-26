# Leetcode: 49. Group Anagrams

import collections

def group_anagrams(strs):
    anagrams = collections.defaultdict(list)
    for s in strs:
        anagrams[tuple(sorted(s))].append(s)

    return list(anagrams.values())

if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["eat","tea","ate"],["tan","nat"],["bat"]]
    print(group_anagrams([""]))
    # [[""]]
    print(group_anagrams(["a"]))
    # [["a"]]
