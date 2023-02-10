class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        lands = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 1]
        visited = set(lands)
        q = deque(lands)
        if len(q) in [0, len(grid) * len(grid[0])]: return -1
        d = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                for nr, nc in neighs:
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            d += 1
        return d - 1