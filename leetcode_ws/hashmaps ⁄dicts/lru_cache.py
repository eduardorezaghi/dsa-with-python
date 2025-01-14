import collections


class LRUCache:
    items: collections.OrderedDict

    def __init__(self, capacity: int):
        self.items = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.items:
            value = self.items.pop(key)
            self.items[key] = value
            return value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.items.pop(key)
        elif len(self.items) >= self.capacity:
            self.items.popitem(last=False)

        self.items[key] = value


