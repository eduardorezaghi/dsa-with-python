class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Given a string, found the length of the longest palindrome.

        # Approach: Expand around center
        # For each character in the string, expand around the center to find the palindrome.
        # The center is either the character itself or the space between two characters.
        # The palindrome can be odd or even length, so we need to consider both cases.
        # Time complexity: O(n^2)
        # Space complexity: O(1)

        def expand_around_center(s: str, left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        if not s:
            return 0

        start = 0
        end = 0
        for i in range(len(s)):
            len1 = expand_around_center(s, i, i)
            len2 = expand_around_center(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

if __name__ == "__main__":
    s = Solution()
    assert s.longestPalindrome("babad") == "bab"