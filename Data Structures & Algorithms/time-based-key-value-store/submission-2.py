class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        res = ""
            
        array = self.hashmap[key]
        l, r = 0, len(array) - 1
        while l <= r:
            m = l + (r - l) // 2

            if array[m][0] > timestamp:
                r = m - 1
            
            elif array[m][0] <= timestamp:
                l = m + 1
                res = array[m][1]
        return res