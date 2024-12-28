def alternatingCharacters(s):
    # Write your code here
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1

    return deletions


if __name__ == '__main__':
    inputs = [
        'ABBABBAA',
    ]

    outputs = [
        3,
        4,
        4
    ]
    
    for i, input_str in enumerate(inputs):
        assert alternatingCharacters(input_str) == outputs[i]
