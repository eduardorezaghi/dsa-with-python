class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L=0
        ARRAY_SIZE = len(nums)
        sum_window = 0
        min_length = float('inf')

        # [1,4,4], target = 5
        for R in range(ARRAY_SIZE):
            # start by summing up and increasing the window size until we reach the target
            sum_window += nums[R]

            while sum_window >= target:
                # if we reach the target, we can shrink the window size
                min_length = min(min_length, R - L + 1)

                # Shrink the window size by removing the leftmost element
                sum_window -= nums[L]
                L += 1 # move the left pointer to the right (check the next window)

        return min_length if min_length != float('inf') else 0