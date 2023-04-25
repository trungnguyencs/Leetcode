from sortedcontainers import SortedSet

class SmallestInfiniteSet:

    def __init__(self):
        self.addedBackSet = SortedSet()
        self.num = 1
        
    def popSmallest(self) -> int: #log(n)
        if self.addedBackSet:
            return self.addedBackSet.pop(0)
        else:
            self.num += 1
            return self.num - 1

    def addBack(self, num: int) -> None: #log(n)
        if num < self.num:
            self.addedBackSet.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)