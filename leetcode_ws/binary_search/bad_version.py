

def is_bad_version(version: int) -> bool:
    global bad_version
    return version >= bad_version

def find_first_bad_version(n: int) -> int:
    def binary_search(left: int, right: int) -> int:
        if left == right:
            return left
            
        mid = left + right // 2
        
        if is_bad_version(mid):
            return binary_search(left, mid)
        else:
            return binary_search(mid + 1, right)

    return binary_search(1, n)


if __name__ == "__main__":
    bad_version = 4
    assert find_first_bad_version(5) == 4