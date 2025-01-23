# Leetcode: 35. Search Insert Position

def search_insert(nums: list, target: int) -> int:
    L,R = 0,len(nums)-1
    
    while L <= R:
        m = (L + R) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            L = m + 1
            # [1,  3,  5,  6]
            #  L   m   R
        else:
            R = m - 1
    
    return L

if __name__ == "__main__":
    # Test cases
    assert search_insert([1,3], 3) == 1
    assert search_insert([1,4], 3) == 1
    # assert search_insert([1,3,5,6], 5) == 2
    # assert search_insert([1,3,5,6], 2) == 1
    # assert search_insert([1,3,5,6], 7) == 4
    # assert search_insert([1,3,5,6], 0) == 0
    

# end