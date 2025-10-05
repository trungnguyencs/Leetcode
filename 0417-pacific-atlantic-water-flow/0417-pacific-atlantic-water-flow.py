class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        pacificQ = deque([(0, c) for c in range(C)] + [(r, 0) for r in range(R)])
        atlanticQ = deque([(R-1, c) for c in range(C)] + [(r, C-1) for r in range(R)])
        pacific = self.bfs(grid, pacificQ)
        atlantic = self.bfs(grid, atlanticQ)
        return list(pacific.intersection(atlantic))

    def bfs(self, grid, q):
        visited = set()
        while q:
            r, c = q.popleft()
            if (r, c) in visited: continue
            visited.add((r, c))
            neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for nr, nc in neighs:
                if (nr, nc) not in visited and\
                 0 <= nr < len(grid) and\
                 0 <= nc < len(grid[0]) and\
                 grid[nr][nc] >= grid[r][c]:
                    q.append((nr, nc))
        return visited