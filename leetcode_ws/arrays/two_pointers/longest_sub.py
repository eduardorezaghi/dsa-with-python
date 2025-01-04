class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Given a string, found the length of the longest substring.
        # "abc abc bb"

        # Sliding window
        # 1. left = 0, right = 0
        # 2. if s[right] in s[left:right] -> left += 1
        # 3. if s[right] not in s[left:right] -> right += 1
        # 4. record the max length of substring

        left = right = 0
        max_length = 0
        while right < len(s):
            if s[right] in s[left:right]:
                left += 1
            else:
                max_length = max(max_length, right - left + 1)
                right += 1
        return max_length