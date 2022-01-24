class MinStack:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mstack = []
        
    def push(self, x: int) -> None:
        if not self.mstack or x <= self.mstack[-1]:
            self.mstack.append(x)
        self.stack.append(x)
​
    def pop(self) -> None:
        if self.stack[-1] == self.mstack[-1]:
            self.mstack.pop()
        return self.stack.pop()
​
    def top(self) -> int:
        return self.stack[-1]
​
    def getMin(self) -> int:
        return self.mstack[-1]
​
​
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
