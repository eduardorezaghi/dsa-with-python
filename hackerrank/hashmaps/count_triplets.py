def countTriplets(arr, rate):
    count = 0
    dict = {}
    dictPairs = {}

    for element in reversed(arr):
        if element*rate in dictPairs:
            count += dictPairs[element*rate]

        if element*rate in dict:
            dictPairs[element] = dictPairs.get(element, 0) + dict[element*rate]

        dict[element] = dict.get(element, 0) + 1

    return count

if __name__ == "__main__":
    arr = [1, 3, 9, 9, 27, 81]
    r = 3
    print(countTriplets(arr, r))  # 6
    arr = [1, 5, 5, 25, 125]
    r = 5
    print(countTriplets(arr, r))  # 4
    arr = [1, 2, 2, 4]
    r = 2
    print(countTriplets(arr, r))  # 2
    arr = [1, 1, 1, 1]
    r = 1
    print(countTriplets(arr, r))  # 0
    arr = [1, 2, 1, 2, 4]
    r = 2
    print(countTriplets(arr, r))  # 3
    arr = [1, 3, 3, 9, 9, 27, 81]
    r = 3
    print(countTriplets(arr, r))  # 10
    arr = [1, 3, 3, 9, 9, 27, 81, 81]
    r = 3
    print(countTriplets(arr, r))  # 16
    arr = [1, 3, 3, 9, 9, 27, 81, 81, 81]
    r = 3
    print(countTriplets(arr, r))  # 22
    arr = [1, 3, 3, 9, 9, 27, 81, 81, 81, 81]
    r = 3
    print(countTriplets(arr, r))  # 26
    arr = [1, 3, 3, 9, 9, 27, 81, 81, 81, 81, 81]
    r = 3
    print(countTriplets(arr, r))  # 30
    arr = [1, 3, 3, 9, 9, 27, 81, 81, 81, 81, 81, 81]
    r = 3
 