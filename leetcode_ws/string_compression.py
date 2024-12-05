def compress(chars: list[str]) -> int:
    j = 0
    i = 0
    chars_len = len(chars)
    while i < chars_len:
        char = chars[i]
        count = 0
        while i < chars_len and chars[i] == char:
            i += 1
            count += 1
        chars[j] = char
        j += 1

        if count > 1:
            for digit in str(count):
                chars[j] = digit
                j += 1
    return j

if __name__ == '__main__':
    chars = ["a", "a", "b", "b"]
    print(compress(chars))  # 4
    print(chars[:4])  # ["a", "2", "b", "2"]