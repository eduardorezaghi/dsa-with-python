# Leetcode: # 26. Remove Duplicates from Sorted Array

def remove_duplicates(nums: list[int]) -> int:
    L = 0

    for R in range(1, len(nums)):
        if nums[L] != nums[R]:
            L += 1
            nums[L] = nums[R]

    return L + 1

if __name__ == "__main__":
    print(remove_duplicates([1, 1, 2]))  # 2