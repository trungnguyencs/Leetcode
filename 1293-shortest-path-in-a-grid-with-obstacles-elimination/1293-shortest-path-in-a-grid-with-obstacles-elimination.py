class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = deque([(0, 0, 0, k)])
        visited = {(0, 0, k)}
        while q:
            r, c, d, bomb = q.popleft()
            if (r, c) == (len(grid) - 1, len(grid[0]) - 1): return d
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc, bomb) not in visited:
                    if grid[nr][nc] == 0:
                        visited.add((nr, nc, bomb))
                        q.append((nr, nc, d+1, bomb))
                    elif bomb > 0:
                        visited.add((nr, nc, bomb))
                        q.append((nr, nc, d+1, bomb-1))
        return -1