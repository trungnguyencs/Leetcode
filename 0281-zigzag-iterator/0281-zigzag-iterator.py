class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.i1 = 0
        self.i2 = 0
        self.v1 = v1
        self.v2 = v2
        self.v1Turn = True

    def next(self) -> int:
        if self.i2 == len(self.v2):
            self.v1Turn = True
        elif self.i1 == len(self.v1):
            self.v1Turn = False
        if self.v1Turn:
            ret = self.v1[self.i1]
            self.i1 += 1
        else:
            ret = self.v2[self.i2]
            self.i2 += 1
        self.v1Turn = not self.v1Turn
        return ret

    def hasNext(self) -> bool:
        return self.i1 < len(self.v1) or self.i2 < len(self.v2)


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())