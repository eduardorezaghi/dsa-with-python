# Leetcode: 53. Maximum Subarray

def max_subarray_sum(arr):
    max_sum = float('-inf')  # Smallest possible number
    current_sum = 0

    for num in arr:
        current_sum += num  # Add current number to running sum
        max_sum = max(max_sum, current_sum)  # Update max sum if needed

        if current_sum < 0:  # If sum becomes negative, reset it
            current_sum = 0

    return max_sum

if __name__ == "__main__":
    print(max_subarray_sum([-2,1,-3])) # 1
    print(max_subarray_sum([-2,7-3,4])) # 8
    print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))  # 6
    print(max_subarray_sum([5,4,-1,7,8])) # 23