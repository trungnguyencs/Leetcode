class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque([(r, c) for r in range(n) for c in range(n) if grid[r][c]])
        if len(q) in [0, n*n]: return -1
        d = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                neigh = ((r-1, c), (r+1, c), (r, c-1), (r, c+1))
                for x, y in neigh:
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 2
                        q.append((x, y))
            d += 1
        return d
