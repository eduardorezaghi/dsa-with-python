def longest_substring(s: str) -> int:
    # Count each different character in the string.
    # If a character is repeated, shrink window.
    # - Update max length as the window grows.
    # - Return max length.

    s_list = list(s)
    L = 0
    max_substr_l = 0
    ARRAY_SIZE = len(s_list)
    char_count = dict()

    for R in range(ARRAY_SIZE):
        if s_list[R] in char_count:
            L = max(L, char_count[s_list[R]] + 1)

        char_count[s_list[R]] = R
        window = R - L + 1
        max_substr_l = max(max_substr_l, window)

    return max_substr_l


if __name__ == "__main__":
    print(longest_substring("abcabcbb"))  # 3
    print(longest_substring("bbbbb"))  # 1