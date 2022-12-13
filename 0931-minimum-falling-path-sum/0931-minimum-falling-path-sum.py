class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix[0]) == 1: return sum(row[0] for row in matrix)
        dp = matrix[0]
        for row in matrix[1:]:
            tmp = [0]*len(dp)
            tmp[0] = row[0] + min(dp[0], dp[1])
            for i in range(1, len(dp) - 1):
                tmp[i] = row[i] + min(dp[i-1], dp[i], dp[i+1])
            tmp[-1] = row[-1] + min(dp[-1], dp[-2])
            dp = tmp
        return min(dp)