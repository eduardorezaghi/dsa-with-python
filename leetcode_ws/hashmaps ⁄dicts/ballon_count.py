def maxNumberOfBalloons(text: str) -> int:
    import collections
    # create a counter for the word "balloon" with all values set to 0
    count = collections.defaultdict(int)
    [count.update({char: 0}) for char in "balloon"]
    
    # Count occurrences of each letter needed for "balloon"
    for char in text:
        if char in count:
            count[char] += 1
    
    # For "balloon", we need 1 b, 1 a, 2 l's, 2 o's, and 1 n
    # Return minimum number of complete "balloon" words possible
    return min(
        count['b'],
        count['a'],
        count['l'] // 2,
        count['o'] // 2,
        count['n']
    )

if __name__ == "__main__":
    print(maxNumberOfBalloons("nlaebolko"))  # 1
    print(maxNumberOfBalloons("loonbalxballpoon"))  # 2