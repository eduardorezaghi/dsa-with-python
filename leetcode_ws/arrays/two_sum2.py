# [1,2,3,9], sum 5, return pair [2,3]
# 



def _two_sum(numbers: list):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                return [numbers[i], numbers[j]]

    # Time complexity: O(n^2)
    # Space complexity: O(1)
    return []

def two_sum(numbers: list):
    numbers.sort()
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == 0:
            return [numbers[left], numbers[right]]
        elif current_sum < 0:
            left += 1
        else:
            right -= 1

    # Time complexity: O(nlogn)
    # Space complexity: O(1)

if __name__ == "__main__":
    import time  
    import random

    start2 = time.time()
    numbers = random.sample(range(1, 1000000000), 10000000)
    print(two_sum(numbers))
    end2 = time.time()
    print(f"Time taken: {end2-start2}")