class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.q = deque([])

    def next(self, val: int) -> float:
        self.sum += val
        self.q.append(val)
        if len(self.q) == self.size + 1:
            self.sum -= self.q.popleft()
        return self.sum/len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)