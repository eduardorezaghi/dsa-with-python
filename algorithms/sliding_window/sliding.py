# Problem:
# Find if two elements in a list/array are equal, for a K fixed size window.
# Example:
# [1, 2, 3, 3], K = 2
# [1,3,4,4,4,5,12,24,36,36], K = 3

def equal(arr, K):
    hash_s = set()
    L = 0

    # for each element in the array.
    for R in range(len(arr)):
        # check if the window size is equal to K (the fixed size we are looking for).
        if R - L == K:
            if arr[R] in hash_s:
                return True
            hash_s.remove(arr[L])
            L += 1

        # add the element to the set (we've seen it).
        hash_s.add(arr[R])

    return False

# Problem:
# Given an array of integers, find the length of the longest subarray that contains the same number of elements.
# Example:
# [1, 2, 3, 3] -> 2
# [4,4,3,3,3,3,2,1] -> 4

# (Variable Sliding Window)

def longest_subarray_length(nums: list[int]) -> int:
    max_len = 0
    L = 0

    for R in range(len(nums)):
        if nums[R] == nums[L]:
            max_len = max(max_len, R - L + 1)
        else:
            L = R

    return max_len


if __name__ == "__main__":
    print(equal([1, 2, 3, 3], 2))  # True
    print(equal([1,3,4,4,4,5,12,24,36,36], 3))  # True

    print(longest_subarray_length([1, 2, 3, 3]))  # 2
    print(longest_subarray_length([4,4,3,3,3,3,2,1]))  # 4