class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c] = int(matrix[r][c])
        maxSquare = 1 if any(matrix[0]) or any([matrix[r][0] for r in range(1, len(matrix))]) else 0
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if not matrix[r][c]: continue
                matrix[r][c] = 1 + min(matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1])
                maxSquare = max(maxSquare, matrix[r][c]**2)
        return maxSquare