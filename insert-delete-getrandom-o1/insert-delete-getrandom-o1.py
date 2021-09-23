class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic: return False
        self.arr.append(val)
        self.dic[val] = len(self.arr) - 1
        return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.dic: return False
        self.dic[self.arr[-1]] = self.dic[val]
        self.arr[self.dic[val]], self.arr[-1] = self.arr[-1], val
        self.arr.pop()
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.arr[randint(0, len(self.arr) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()