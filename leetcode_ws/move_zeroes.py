def move_zeroes(arr: list):
    if len(arr) == 0:
        return 0

    # [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
    i = 0
    j = 0
    while j < len(arr):
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1

        j += 1

    while i < len(arr):
        arr[i] = 0
        i += 1

    return arr