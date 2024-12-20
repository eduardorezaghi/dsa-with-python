import functools
from timeit import timeit


def nth_fibonacci(n):
    if n == 0 or n == 1:
        return n

    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

@functools.lru_cache(maxsize=None)
def memoized_nth_fibonacci(n):
    if n == 0 or n == 1:
        return n

    return memoized_nth_fibonacci(n - 1) + memoized_nth_fibonacci(n - 2)


if __name__ == '__main__':
    n = 40
    no_cache = timeit(lambda: nth_fibonacci(n), number=1)
    with_cache = timeit(lambda: memoized_nth_fibonacci(n), number=1)
    
    print(f"Time taken without cache: {no_cache:.10f}")
    print(f"Time taken with cache: {with_cache:.10f}")