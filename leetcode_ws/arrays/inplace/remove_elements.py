def remove_element(nums: list[int], val: int) -> int:
    remaining_elements = 0
    for i,v in enumerate(nums):
        if v == val:
            nums[i] = '_'
        else:
            remaining_elements += 1

    [nums.remove('_') for _ in range(nums.count('_'))]

    return remaining_elements


# def remove_element(nums: list[int], val: int) -> int:
#     write_index = 0
#     for _,v in enumerate(nums):
#         if v != val:
#             write_index += 1
#         else:
#             del nums[write_index]
#             nums.append('_')

#     return write_index


if __name__ == "__main__":
    # Example 1:
    # Input: arr1 = [3,2,2,3], val = 3
    # Output: 2, arr1 = [2,2,_,_]
    print(remove_element([3, 2, 2, 3], 3))  # 2
    print(remove_element([0,1,2,2,3,0,4,2], 2)) # 5, [0,1,3,0,4,_,_,_]