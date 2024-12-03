class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None]*n
        self.l = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey - 1] = value
        r = self.l
        ans = []
        while r < len(self.arr) and self.arr[r] != None:
            ans.append(self.arr[r])
            r += 1
        self.l = r
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)