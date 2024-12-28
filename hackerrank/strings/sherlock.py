def isValid(s):
    s_classf = {}
    for idx,char in enumerate(s):
        if char == s[idx+1]:
            s_classf[char] += 1

    rem_count = 0
    for _, count in s_classf.items():
        if count == 1:
            continue
        elif count == 2:
            rem_count += 1
            continue
        elif count >= 3:
            return "NO"
    
    if rem_count > 1:
        return "NO"

    return "YES"



if __name__ == "__main__":
    inputs = [
        "abc",  # "YES"
        "abcc", # "YES"
        "abbbc",# "NO",
        "aabbc", # "NO"
        "abcdefghhgfedecba" # "YES"
    ]
    
    for i in inputs:
        print(isValid(i))
