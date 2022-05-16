class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        q = deque([(0, 0, 1)])
        grid[0][0] = '#'
        neighs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        while q:
            r, c, d = q.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1: return d
            for dr, dc in neighs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0:
                    q.append((nr, nc, d + 1))
                    grid[nr][nc] = '#'
        return -1