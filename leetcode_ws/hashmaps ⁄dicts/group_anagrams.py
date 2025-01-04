# Leetcode: 49. Group Anagrams

import collections

def group_anagrams(strs):
    anagrams = collections.defaultdict(list)
    for s in strs:
        anagrams[tuple(sorted(s))].append(s)

    return list(anagrams.values())