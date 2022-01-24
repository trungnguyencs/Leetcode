class FreqStack:

    def __init__(self):
        self.counter = Counter()
        self.stackOfStacks = []

    def push(self, x: int) -> None:
        self.counter[x] += 1
        if self.counter[x] > len(self.stackOfStacks):
            self.stackOfStacks.append([])
        self.stackOfStacks[self.counter[x] - 1].append(x)
        
    def pop(self) -> int:
        popped = self.stackOfStacks[-1].pop()
        self.counter[popped] -= 1
        if not self.stackOfStacks[-1]:
            self.stackOfStacks.pop()
        return popped


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()