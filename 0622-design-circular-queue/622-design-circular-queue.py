class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [0]*k
        self.start = self.len = 0
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.len += 1
        i = (self.start + self.len - 1) % self.k
        self.arr[i] = value
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.len -= 1
        self.start = (self.start + 1) % self.k
        return True

    def Front(self) -> int:
        if self.len == 0: return -1
        return self.arr[self.start]

    def Rear(self) -> int:
        if self.len == 0: return -1
        i = (self.start + self.len - 1) % self.k
        return self.arr[i]
    
    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()