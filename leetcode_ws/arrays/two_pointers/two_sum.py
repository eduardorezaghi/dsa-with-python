def two_sum(arr: list[int], target: int) -> list[int]:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    """
    num_to_index = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    target = 8
    print(two_sum(arr, target))  # [0, 6]

    # non-sorted list
    arr = [8, 1, 5, 2, 6, 3, 4]
    target = 10
    print(two_sum(arr, target))  # [0, 4]