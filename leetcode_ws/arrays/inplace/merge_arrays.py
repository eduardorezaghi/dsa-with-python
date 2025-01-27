def merge_arrays(nums1: list[int], nums2: list[int], m: int, n: int) -> list[int]:
    ARRAY_SIZE = m + n
    write_index = ARRAY_SIZE - 1
    L = m - 1
    R = n - 1

    while L >= 0 and R >= 0:
        if nums1[L] > nums2[R]:
            nums1[write_index] = nums1[L]
            L -= 1
        else:
            nums1[write_index] = nums2[R]
            R -= 1

        write_index -= 1

    return nums1

if __name__ == "__main__":
    # Example 1:
    # Input: arr1 = [1, 3, 5, 7], arr2 = [0, 2, 6, 8, 9], arr1_size = 4, arr2_size = 5
    # Output: [0, 1, 2, 3, 5, 6, 7, 8, 9]
    print(merge_arrays([1, 3, 5, 7], [0, 2, 6, 8, 9], 4, 5))  # [0, 1, 2, 3, 5, 6, 7, 8, 9]