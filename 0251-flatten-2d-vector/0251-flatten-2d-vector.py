class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.outer = self.inner = 0

    def next(self) -> int:
        if self.hasNext():
            ret = self.vec[self.outer][self.inner]
            self.inner += 1
            return ret
        
    def hasNext(self) -> bool:
        while self.outer != len(self.vec) and self.inner == len(self.vec[self.outer]):
            self.inner = 0
            self.outer += 1
        return self.outer != len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()