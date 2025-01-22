class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R, C = len(isWater), len(isWater[0])
        grid = [[-1]*C for _ in range(R)]
        q = deque([])
        visited = set()
        for r in range(R):
            for c in range(C):
                if isWater[r][c] == 1:
                    grid[r][c] = 0
                    q.append((r, c, 0))
                    visited.add((r, c))
        while q:
            r, c, h = q.popleft()
            neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for nr, nc in neighs:
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                    grid[nr][nc] = h + 1
                    q.append((nr, nc, h + 1))
                    visited.add((nr, nc))
        return grid