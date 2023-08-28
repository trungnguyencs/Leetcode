# class MyStack: # O(n) push; O(1) pop, top

#     def __init__(self):
#         self.q = deque()

#     def push(self, x: int) -> None:
#         self.q.append(x)
#         for _ in range(len(self.q) - 1):
#             self.q.append(self.q.popleft())
        
#     def pop(self) -> int:
#         return self.q.popleft()
            
#     def top(self) -> int:
#         return self.q[0]

#     def empty(self) -> bool:
#         return len(self.q) == 0

class MyStack: # O(1) push; O(n) pop, top

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        
    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        return self.q.popleft()
    
    def top(self) -> int:
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        ret = self.q[0]
        self.q.append(self.q.popleft())
        return ret
    
    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()