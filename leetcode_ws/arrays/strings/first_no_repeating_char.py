# Leetcode: 387. First Unique Character in a String
# link: https://leetcode.com/problems/first-unique-character-in-a-string/

def firstUniqChar(s: str) -> int:
    from collections import Counter
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


# A variation of this question was asked in Amazon's OA,
# where they asked to return the first non-repeating character.

def firstUniqChar(s: str) -> int:
    from collections import Counter
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return c # simply return the character
    return -1