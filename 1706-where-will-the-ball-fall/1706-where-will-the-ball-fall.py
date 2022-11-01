class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        pos = [c for c in range(C)]
        for row in grid:
            for c, p in enumerate(pos):
                if p == -1: continue
                if row[p] == 1:
                    pos[c] = -1 if (p == C - 1 or row[p+1] == -1) else p + 1
                else:
                    pos[c] = -1 if (p == 0 or row[p-1] == 1) else p - 1
        return pos