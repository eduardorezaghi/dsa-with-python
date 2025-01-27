def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """   
    ARRAY_SIZE = len(nums)
    k = k % ARRAY_SIZE
    write_index = ARRAY_SIZE - 1
    L = ARRAY_SIZE - k - 1
    R = ARRAY_SIZE - 1

    while L >= 0 and R >= 0:
        nums[write_index] = nums[L]
        write_index -= 1
        L -= 1

    write_index = k - 1
    L = ARRAY_SIZE - 1
    while write_index >= 0 and L >= 0:
        nums[write_index] = nums[L]
        write_index -= 1
        L -= 1

    return nums

if __name__ == "__main__":
    # Example 1:
    # Input: nums = [1,2,3], k = 2
    # Output: [2,3,1]
    print(rotate([1, 2, 3], 2))  # [2,3,1]
