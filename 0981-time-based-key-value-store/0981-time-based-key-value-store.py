class TimeMap:

    def __init__(self):
        self.dic = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = [[], []]
        self.dic[key][0].append(timestamp)
        self.dic[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic: return ''
        timestamps, values = self.dic[key]
        i = bisect_right(timestamps, timestamp)
        return '' if i == 0 else values[i - 1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)