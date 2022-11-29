class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val in self.dic: return False
        self.arr.append(val)
        self.dic[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic: return False
        i = self.dic[val]
        self.arr[i], self.dic[self.arr[-1]] = self.arr[-1], i
        self.arr.pop()
        del self.dic[val]
        return True
        
    def getRandom(self) -> int:
        return self.arr[randint(0, len(self.arr) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()