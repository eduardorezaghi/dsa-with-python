# Leetcode: 981. Time Based Key-Value Store
# link: https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append({"value": value, "timestamp": timestamp})

    def get(self, key: str, timestamp: int) -> str:
        value, values = "", self.storage.get(key, [])
        
        l, r = 0, len(values) - 1
        while l <= r:
            mid = l + (r - l) // 2 # to avoid overflow
            if values[mid]["timestamp"] == timestamp:
                return values[mid]["value"]
            elif values[mid]["timestamp"] < timestamp:
                l = mid + 1
            else:
                r = mid - 1

        return value

if __name__ == "__main__":
    # ["TimeMap", "set", ["test", "one", 10], "set", ["test", "two", 20], "set", ["test", "three", 30], "get", ["test", 15], "get", ["test", 25], "get", ["test", 35]]
    t = TimeMap()
    t.set("test", "one", 10)
    t.set("test", "two", 20)
    t.set("test", "three", 30)
    print(t.get("test", 15)) # one
    print(t.get("test", 25)) # two
    print(t.get("test", 35)) # three
    print(t.get("test", 5))  # ""
    print(t.get("test", 40)) # ""