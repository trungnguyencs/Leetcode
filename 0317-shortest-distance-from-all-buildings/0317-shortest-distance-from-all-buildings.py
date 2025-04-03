class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # first element is the total distance, second element is number of accessible buildings
        R, C = len(grid), len(grid[0])
        distances = [[[0, 0] for _ in range(C)] for _ in range(R)]
        buildings = set([(r, c) for r in range(R) for c in range(C) if grid[r][c] == 1])
        obstacles = set([(r, c) for r in range(R) for c in range(C) if grid[r][c] == 2])
        self.updateDistanceMap(grid, distances, buildings, obstacles)
        return min([distances[r][c][0] for r in range(R) for c in range(C) if distances[r][c][1] == len(buildings)], default=-1)

    def updateDistanceMap(self, grid, distances, buildings, obstacles):
        for r, c in buildings:
            visited = set([(r, c)])
            q = deque([(r, c, 0)])
            while q:
                r, c, d = q.popleft()
                neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                for nr, nc in neighs:
                    if 0 <= nr < len(grid)\
                    and 0 <= nc < len(grid[0])\
                    and (nr, nc) not in visited\
                    and (nr, nc) not in buildings\
                    and (nr, nc) not in obstacles:
                        visited.add((nr, nc))
                        q.append((nr, nc, d + 1))
                        distances[nr][nc][0] += d + 1
                        distances[nr][nc][1] += 1