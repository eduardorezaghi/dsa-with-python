def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_dict = {}
    t_dict = {}

    for char in s:
        s_dict[char] = s_dict.get(char, 0) + 1
    
    for char in t:
        t_dict[char] = t_dict.get(char, 0) + 1

    return s_dict == t_dict

if __name__ == '__main__':
    print(valid_anagram('anagram', 'nagaram'))  # True
    print(valid_anagram('rat', 'car'))  # False
    print(valid_anagram('a', 'ab'))  # False
    print(valid_anagram('aacc', 'cccx'))  # False