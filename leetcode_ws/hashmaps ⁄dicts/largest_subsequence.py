def largest_subsequence(nums: list[int]) -> int:
    items = set(nums)

    largest = 0
    for n in nums:
        if n - 1 in items:
            continue
        else:
            current = n
            while current in items:
                current += 1
            largest = max(largest, current - n)

    return largest

if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    print(largest_subsequence(nums))  # 4
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(largest_subsequence(nums))  # 9