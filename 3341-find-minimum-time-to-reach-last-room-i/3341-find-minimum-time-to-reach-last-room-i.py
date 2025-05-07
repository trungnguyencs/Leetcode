class Solution:
    def minTimeToReach(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        heap = [(0, 0, 0)]
        visited = {}
        while heap:
            time, r, c = heappop(heap)
            neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for nr, nc in neighs:
                if not 0 <= nr < R or not 0 <= nc < C: continue
                if (nr, nc) not in visited or time + 1 < visited[(nr, nc)]:
                    nextTime = max(grid[nr][nc] + 1, time + 1)
                    heappush(heap, (nextTime, nr, nc))
                    visited[(nr, nc)] = nextTime
        return visited[(R - 1, C - 1)]