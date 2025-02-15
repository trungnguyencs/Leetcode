from sortedcontainers import SortedList

class MRUQueue:

    def __init__(self, n: int):
        self.list = SortedList()
        for i in range(1, n + 1):
            self.list.add((i, i))
        self.timestamp = i

    def fetch(self, k: int) -> int:
        self.timestamp += 1
        _, num = self.list.pop(k - 1)
        self.list.add((self.timestamp, num))
        return num


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)