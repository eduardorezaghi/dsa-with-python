# Leetcode: 162. Find Peak Element
# link: https://leetcode.com/problems/find-peak-element/

import math

# BINARY SEARCH: General approach
# 1. Initialize left and right pointers (search space)

# 2. While left < right:
#    - Calculate mid
#    - If mid is the peak, return mid
#    - If mid is not the peak, update left or right based on the condition

# 3. Return left

def findPeak(nums: int) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = math.floor((left + right) / 2)

        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left

def recursiveFindPeak(nums: int, left: int, right: int) -> int:
    if left == right:
        return left

    mid = (left + right) // 2

    if nums[mid] > nums[mid + 1]:
        return recursiveFindPeak(nums, left, mid)
    else:
        return recursiveFindPeak(nums, mid + 1, right)