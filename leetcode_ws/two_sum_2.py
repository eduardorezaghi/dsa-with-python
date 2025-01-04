# Leetcode: 167. Two Sum II - Input array is sorted

# Problem:
# Given an array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.


def two_sum_ii(numbers: list[int], target: int) -> list[int]:
    L,R = 0, len(numbers)-1

    
    while L < R:
        if (numbers[L] + numbers[R]) == target:
            break
        elif (numbers[L] + numbers[R]) < target:
            L += 1
        elif (numbers[L] + numbers[R]) > target:
            R -= 1

    return [L+1,R+1]

if __name__ == "__main__":
    print(two_sum_ii([2,7,11,15], 9))  # [1,2]
    print(two_sum_ii([2,3,4], 6))  # [1,3]

    assert two_sum_ii([2,7,11,15], 9) == [1,2]
    assert two_sum_ii([2,3,4], 6) == [1,3]
    assert two_sum_ii([-1,0], -1) == [1,2]
    assert two_sum_ii([5,25,75], 100) == [2,3]
    assert two_sum_ii([1,2,3,4,4,9,56,90], 8) == [4,5]
    assert two_sum_ii([1,2,3,4,4,9,56,90], 17) == [6,7]
    assert two_sum_ii([1,2,3,4,4,9,56,90], 65) == [7,8]
    assert two_sum_ii([1,2,3,4,4,9,56,90], 99) == [7,8]
    assert two_sum_ii([1,2,3,4,4,9,56,90], 100) == [7,8]
    print("All tests passed!")