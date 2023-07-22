class Solution:
    def knightProbability(self, n: int, k: int, r0: int, c0: int) -> float:
        if k == 0: return 1
        dp = [[0]*n for _ in range(n)]
        dp[r0][c0] = 1
        neighs = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
        for _ in range(k):
            newDp = [[0]*n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for dr, dc in neighs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            newDp[nr][nc] += dp[r][c]/8.0
            dp = newDp
        return sum(sum(row) for row in dp)