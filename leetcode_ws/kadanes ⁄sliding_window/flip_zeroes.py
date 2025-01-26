def longest_ones(nums: list[int], k: int) -> int:
    # Sliding window.
    # - Count of zeros.

    L = 0
    max_len = 0
    zero_count = 0

    ARR_SIZE = len(nums)
    for R in range(ARR_SIZE):
        if nums[R] == 0:
            zero_count += 1

        # If zero count exceeds k, shrink window.
        while zero_count > k:
            if nums[L] == 0:
                zero_count -= 1
            L += 1

        max_len = max(max_len, R - L + 1)
    return max_len