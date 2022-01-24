class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == y == 0: return 0
        visited = set([(0, 0)])
        q = deque([(0, 0, 0)])
        while q:
            r, c, d = q.popleft()
            neighs = [(r-2, c-1), (r-2, c+1), (r+2, c-1), (r+2, c+1),\
                      (r-1, c-2), (r-1, c+2), (r+1, c-2), (r+1, c+2)]
            for nr, nc in neighs:
                if (nr, nc) in visited: continue
                if [abs(nr), abs(nc)] == [abs(x), abs(y)]: return d + 1
                visited.add((nr, nc))
                q.append((nr, nc, d + 1))