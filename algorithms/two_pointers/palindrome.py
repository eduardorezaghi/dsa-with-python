def is_palindrome(s: str) -> bool:
    import re
    # lowercase the string so the ords can be compared.
    s = s.lower()
    # clear out any non-alphanumeric characters.
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    L, R = 0, len(s) - 1
    print(s)
    
    # iterate through.
    while L < R:
        # Compare the ords (ASCII values) of the characters.
        # If they're different, it's not a palindrome. Then, return False.
        if ord(s[L]) != ord(s[R]):
            return False

        # Move the pointers to the next characters.
        L += 1
        R -= 1

    return True



if __name__ == "__main__":
    print(is_palindrome("tababat"))  # True
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("hello"))  # False
    print(is_palindrome("mattam!"))  # True
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True