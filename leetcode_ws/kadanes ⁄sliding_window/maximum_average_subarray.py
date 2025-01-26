class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Sum of first k elements.
        curr_sum = max_sum = sum(nums[:k])

        # Sliding window.
        # - Subtract previous element.
        # - Add new element.
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)

        return max_sum / k

if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAverage([1,12,-5,-6,50,3], 4))  # 12.75
    print(s.findMaxAverage([5], 1))  # 5.0

    ...