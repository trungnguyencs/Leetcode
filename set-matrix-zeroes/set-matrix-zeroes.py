class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        firstRowHasZero = firstColHasZero = False
        for r in range(R):
            if not matrix[r][0]:
                firstColHasZero = True
                break
        for c in range(C):
            if not matrix[0][c]:
                firstRowHasZero = True
                break
        for r in range(1, R):
            for c in range(1, C):
                if not matrix[r][c]:
                    matrix[0][c] = matrix[r][0] = 0
        for r in range(1, R):
            if not matrix[r][0]:
                for c in range(1, C):
                    matrix[r][c] = 0
        for c in range(1, C):
            if not matrix[0][c]:
                for r in range(1, R):
                    matrix[r][c] = 0
        if firstColHasZero:
            for r in range(R):
                matrix[r][0] = 0
        if firstRowHasZero:
            for c in range(C):
                matrix[0][c] = 0