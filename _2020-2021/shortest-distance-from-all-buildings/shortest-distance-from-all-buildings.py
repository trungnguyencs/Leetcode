class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # first is total distance, second element is number of accessible buildings
        distances = [[[0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))] 
        buildings = set([(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 1])
        obstacles = set([(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 2])
        for r, c in buildings:
            self.bfs(r, c, distances, buildings, obstacles)
        return min([distances[r][c][0] for r in range(len(distances)) for c in range(len(distances[0])) if distances[r][c][1] == len(buildings)], default=-1)
    
    def bfs(self, r, c, distances, buildings, obstacles):
        q = deque([(r, c, 0)])
        visited = set([(r, c)])
        while q:
            r, c, d = q.popleft()
            neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for nr, nc in neighs:
                if 0 <= nr < len(distances) and 0 <= nc < len(distances[0]) and (nr, nc) not in visited and (nr, nc) not in buildings and (nr, nc) not in obstacles:
                    distances[nr][nc][0] += d + 1
                    distances[nr][nc][1] += 1
                    q.append((nr, nc, d + 1))
                    visited.add((nr, nc))