class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        r0, c0 = self.findStartLocation(grid)
        visited = set([(r0, c0)])
        q = deque([(r0, c0, 0)])
        while q:
            r, c, d = q.popleft()
            neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for nr, nc in neighs:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == '#':
                        return d + 1
                    if grid[nr][nc] == 'O' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc, d + 1))
        return -1

    def findStartLocation(self, grid):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '*':
                    return (r, c)