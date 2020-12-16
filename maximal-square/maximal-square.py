class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        ans = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                upper = int(matrix[r-1][c]) if r > 0 else 0
                left = int(matrix[r][c-1]) if c > 0 else 0
                upperleft = int(matrix[r-1][c-1]) if r > 0 and c > 0 else 0
                if matrix[r][c] == "1":
                    matrix[r][c] = 1 + min(upper, left, upperleft)
                    ans = max(ans, matrix[r][c])
        return ans**2
