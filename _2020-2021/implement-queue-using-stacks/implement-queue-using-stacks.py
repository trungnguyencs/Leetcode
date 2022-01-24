class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1, self.s2 = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.s1) > 1: self.s2.append(self.s1.pop())
        ret = self.s1.pop()
        while self.s2: self.s1.append(self.s2.pop())
        return ret
    
    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s1[0] if self.s1 else self.s2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1 and not self.s2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()