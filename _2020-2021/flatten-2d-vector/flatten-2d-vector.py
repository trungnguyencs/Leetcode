class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.v = vec
        self.x = self.y = 0

    def next(self) -> int:
        if self.hasNext():
            ret = self.v[self.x][self.y]
            self.y += 1
            return ret

    def hasNext(self) -> bool:
        while self.x < len(self.v) and self.y == len(self.v[self.x]):
            self.y = 0
            self.x += 1
        return self.x < len(self.v)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()