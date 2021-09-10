class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        copy = deepcopy(grid)
        q = deque([(row, col)])
        visited = set([(row, col)])
        while q:
            r, c = q.popleft()
            if self.isBorder(r, c, grid):
                copy[r][c] = color
            neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for nr, nc in neighs:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] == grid[r][c]:
                    q.append((nr, nc))
                    visited.add((nr, nc))
        return copy
            
    def isBorder(self, r, c, grid):
        neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighs:
            if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]) or grid[nr][nc] != grid[r][c]:
                return True
        return False