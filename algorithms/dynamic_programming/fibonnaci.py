import functools


@functools.lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

# Tabulated version of Fibonacci
def fib_tab(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    prev = 0
    curr = 1

    for i in range(2, n+1):
        prev, curr = curr, prev + curr

    return curr