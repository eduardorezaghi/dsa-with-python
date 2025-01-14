class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        middle = len(nums) // 2

        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            result = self.search(nums[middle + 1:], target)
            return middle + 1 + result if result != -1 else -1
        else:
            return self.search(nums[:middle], target)