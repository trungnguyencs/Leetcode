class FreqStack:

    def __init__(self):
        self.stackOfStacks = []
        self.counter = Counter()

    def push(self, val: int) -> None:
        self.counter[val] += 1
        if self.counter[val] > len(self.stackOfStacks):
            self.stackOfStacks.append([])
        self.stackOfStacks[self.counter[val] - 1].append(val)

    def pop(self) -> int:
        ans = self.stackOfStacks[-1].pop()
        self.counter[ans] -= 1
        if not self.stackOfStacks[-1]:
            self.stackOfStacks.pop()
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()