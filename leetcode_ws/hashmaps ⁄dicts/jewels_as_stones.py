# Leetcode 771. Jewels and Stones

def numJewelsInStones(self, jewels: str, stones: str) -> int:
    jewels_set = set(jewels)
    count = sum([1 for stone in stones if stone in jewels_set])
    return count