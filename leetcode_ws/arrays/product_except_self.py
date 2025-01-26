def product_except_self(nums: list[int]) -> list[int]:
    import functools
    
    reduced_list = [0] * len(nums)
    
    for i in range(len(nums)):
        reduced_list[i] = functools.reduce(lambda x, y: x * y, nums[:i] + nums[i+1:])

    return reduced_list


if __name__ == "__main__":
    # Example 1:
    # Input: nums = [1,2,3,4]
    # Output: [24,12,8,6]
    print(product_except_self([1, 2, 3, 4]))  # [24,12,8,6]