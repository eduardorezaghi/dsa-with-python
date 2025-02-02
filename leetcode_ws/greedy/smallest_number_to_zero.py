class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest_number = nums[0]
        for n in nums:
            if abs(n) < abs(closest_number) or (abs(n) == abs(closest_number) and n > closest_number):
                closest_number = n

        return closest_number