class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.pointers = deque() #k vectors: use a queue of pointers
        if v1:
            self.pointers.append((0, 0))
        if v2:
            self.pointers.append((1, 0))

    def next(self) -> int:
        v, i = self.pointers.popleft()
        ret = self.vectors[v][i]
        i += 1
        if i < len(self.vectors[v]):
            self.pointers.append((v, i))
        return ret

    def hasNext(self) -> bool:
        return len(self.pointers) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())