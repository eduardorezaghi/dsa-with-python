def rec_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and rec_palindrome(s[1:-1])


if __name__ == '__main__':
    print(rec_palindrome("madam"))  # True
    print(rec_palindrome("racecar"))  # True
    print(rec_palindrome("a"))  # True
    print(rec_palindrome("ab"))  # False
    print(rec_palindrome("abc"))  # False
    print(rec_palindrome("abba"))  # True
    print(rec_palindrome("abcba"))  # True
    print(rec_palindrome("abccba"))  # True
    print(rec_palindrome("abcccb"))  # False
    print(rec_palindrome("abccdc"))  # False
    print(rec_palindrome("abccdcba"))  # True