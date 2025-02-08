from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.numToIndexes = defaultdict(SortedList)
        self.indexToNum = {}

    def change(self, index: int, num: int) -> None:
        if index in self.indexToNum:
            oldNum = self.indexToNum[index]
            self.numToIndexes[oldNum].remove(index)
        self.indexToNum[index] = num
        self.numToIndexes[num].add(index)

    def find(self, num: int) -> int:
        if num not in self.numToIndexes or len(self.numToIndexes[num]) == 0:
            return -1
        return self.numToIndexes[num][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)