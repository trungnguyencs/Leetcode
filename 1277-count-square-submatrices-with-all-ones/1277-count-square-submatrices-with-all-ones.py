class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = copy.deepcopy(matrix)
        R, C = len(matrix), len(matrix[0])
        for r in range(1, R):
            for c in range(1, C):
                if matrix[r][c] == 0:
                    continue
                matrix[r][c] = 1 + min(matrix[r-1][c-1], matrix[r-1][c], matrix[r][c-1])
        return sum(sum(row) for row in matrix)