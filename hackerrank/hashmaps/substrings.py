import collections


def two_strings(s1: str, s2: str):
    freq_1 = collections.defaultdict(int)
    freq_2 = collections.defaultdict(int)

    for char in s1:
        freq_1[char] += 1

    for char in s2:
        freq_2[char] += 1
    
    print(freq_1)
    print(freq_2)
    
    if any([char in freq_1 for char in freq_2]):
        print("YES")
    else:
        print("NO")



if __name__ == "__main__":
    s1 = "ab"
    s2 = "aa"
    two_strings(s1, s2)
