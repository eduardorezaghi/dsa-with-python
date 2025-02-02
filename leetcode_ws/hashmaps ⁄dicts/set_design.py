# Leetcode: 380. Insert Delete GetRandom O(1)
# link: https://leetcode.com/problems/insert-delete-getrandom-o1/

# ps: also discussed on Neetcode: https://www.youtube.com/watch?v=46dZH7LDbf8


class RandomizedSet:
    def __init__(self):
        self._set = dict()
        self._list = []

    def insert(self, val: int) -> bool:
        if val not in self._set:
            self._list.append(val)
            self._set[val] = len(self._list) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self._set:
            el_index = self._set.get(val)
            last_element = self._list[-1]
            self._list[el_index] = last_element
            self._set[last_element] = el_index
            self._list.pop()
            del self._set[val]
            return True
        return False

    def getRandom(self) -> int:
        import random
        return random.sample(self._list, 1)[0]