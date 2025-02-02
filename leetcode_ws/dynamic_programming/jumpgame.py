# Leetcode 55. Jump Game
# link: https://leetcode.com/problems/jump-game/

import functools


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        # shift the goal to the left if the current index can reach the goal.
        # greedy approach: always choose the farthest index that can reach the goal.
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
    
    def minNumberOfJumps(self, nums: list[int]) -> int:
        """
        Find the minimum number of jumps to reach the last index.
        Example:
        Input: nums = [2,3,1,1,4]
        Output: 2,
        Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
        """
        @functools.lru_cache(None)
        def dp(i):
            if i == len(nums) - 1:
                return 0

            if nums[i] == 0:
                return float("inf")

            min_jumps = float("inf")
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    min_jumps = min(min_jumps, 1 + dp(i + j))

            return min_jumps

        return dp(0)