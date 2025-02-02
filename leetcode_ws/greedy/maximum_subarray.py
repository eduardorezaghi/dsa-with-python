


def maximum_subarray(nums: list[int]) -> int:
    if not nums:
        return 0

    # Kadane's algorithm
    max_sum, current_sum = nums[0], nums[0] # suppose the first element is the max sum

    # start from the second element
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    # Time complexity: O(n), n is the length of the input list
    # Space complexity: O(1), only two variables are used

    return max_sum

def maximum_subarray_interval(nums: list[int]) -> tuple[int, int]:
    """Find the maximum subarray sum and the interval of the subarray.
    """
    if not nums:
        return 0, 0

    max_sum, current_sum = nums[0], nums[0] # suppose the first element is the max sum
    L, R = 0, 0 # interval
    
    # start from the second element
    start = 0
    for i, num in enumerate(nums[1:], 1):
        if num > current_sum + num:
            start = i
            current_sum = num
        else:
            current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            L = start
            R = i

    return max_sum, nums[L:R+1]

if __name__ == "__main__":
    print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4])) # 6
    print(maximum_subarray([1])) # 1
    print(maximum_subarray([5,4,-1,7,8])) # 23
    
    print(maximum_subarray_interval([-2,1,-3,4,-1,2,1,-5,4])) # (6, [4, -1, 2, 1])
    print(maximum_subarray_interval([1])) # (1, [1])

