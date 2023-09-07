class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        start = self.findStartPoint(grid)
        visited = {start}
        q = deque([(start, 0)])
        while q:
            (r, c), d = q.popleft()
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] in 'O#':
                    if grid[nr][nc] == '#': return d + 1
                    visited.add((nr, nc))
                    q.append([(nr, nc), d + 1])
        return -1
    
    def findStartPoint(self, grid):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '*': return (r, c)