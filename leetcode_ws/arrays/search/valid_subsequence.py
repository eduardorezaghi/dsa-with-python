# Leetcode: 392. Is Subsequence

class Solution():
    def valid_subsequence(self, array: list[int], sequence: list[int]) -> bool:
        i = 0
        for num in array:
            # Check if we verified all elements in the sequence.
            if num == sequence[i]:
                i += 1
            # Check if we verified all elements in the sequence.
            if i == len(sequence):
                return True
    
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in t:
            if char == s[i]:
                i += 1
            if i == len(s):
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))