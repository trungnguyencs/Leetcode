class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        smallest = s
        q = deque([s])
        visited = set([s])
        while q:
            cur = q.popleft()
            smallest = min(smallest, cur)
            nxt1 = self.addToOddIndices(cur, a)
            nxt2 = self.shift(cur, b)
            self.add(nxt1, visited, q)
            self.add(nxt2, visited, q)
        return smallest

    def addToOddIndices(self, s, a):
        digits = list(s)
        for i in range(1, len(s), 2):
            digits[i] = str((int(digits[i]) + a) % 10)
        return ''.join(digits)

    def shift(self, s, b):
        return s[-b :] + s[: -b]

    def add(self, s, visited, q):
        if s in visited: return
        visited.add(s)
        q.append(s)         