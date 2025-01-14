# Leetcode: 11. Container With Most Water

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        L, R = 0, len(height) - 1

        while L < R:
            local_min = min(height[L], height[R])

            max_area = max(max_area, local_min * (R - L))
            if height[L] < height[R]:
                L += 1
            R -= 1

        return max_area

if __name__ == '__main__':
    s = Solution()
    assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert s.maxArea([1,1]) == 1

    # assert s.maxArea([4,3,2,1,4]) == 16
    # assert s.maxArea([1,2,1]) == 2
    # assert s.maxArea([1,2,4,3]) == 4
    # assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
