class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshCount = 0
        q = deque([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    freshCount += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        if freshCount == 0: return 0
        time = -1
        while q:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                for nr, nc in neighs:
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
        return -1 if any(grid[r][c] == 1 for r in range(len(grid)) for c in range(len(grid[0]))) else time
            
        