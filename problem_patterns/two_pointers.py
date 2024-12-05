def count_unique_values(arr: list):
    if len(arr) == 0:
        return 0

    # [1,2,3] -> 3
    i = 0
    j = 1
    while j < len(arr):
        # if the values are the same, move both pointers
        if arr[i] == arr[j]:
            j += 1
            continue

        elif arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    return i + 1

if __name__ == '__main__':
    print(count_unique_values([1, 1, 1, 1, 1, 2]))  # 2
    print(count_unique_values([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]))  # 7
    print(count_unique_values([]))  # 0
    print(count_unique_values([1]))  # 1
    print(count_unique_values([1, 2]))  # 2
    print(count_unique_values([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))  # 1
    print(count_unique_values([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]))  # 3
    print(count_unique_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 10
    print(count_unique_values([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]))  # 4
    print(count_unique_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]))  # 10