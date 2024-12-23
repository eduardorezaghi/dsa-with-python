import functools


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

@functools.lru_cache(maxsize=None)
def memoized_merge_sort(arr):
    # Convert unhashable list to hashable tuple
    arr = tuple(arr)
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = memoized_merge_sort(arr[:mid])
    right = memoized_merge_sort(arr[mid:])

    return tuple(merge(list(left), list(right)))


if __name__ == '__main__':
    import timeit

    test_setup = '''
from __main__ import merge_sort, memoized_merge_sort
import random

arr = random.sample(range(1, 1000000), 100)
'''
    
    non_memoized = timeit.timeit('merge_sort(arr.copy())', 
                                setup=test_setup, 
                                number=1000)
    memoized = timeit.timeit('memoized_merge_sort(tuple(arr))', 
                            setup=test_setup, 
                            number=1000)

    print(f"Time taken without memoization: {non_memoized:.10f}")
    print(f"Time taken with memoization: {memoized:.10f}")
