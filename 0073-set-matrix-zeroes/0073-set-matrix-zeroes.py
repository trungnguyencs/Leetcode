class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        firstRowHasZero = not all(matrix[0])
        firstColHasZero = False
        for r in range(rows):
            if matrix[r][0] == 0:
                firstColHasZero = True
                break
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0], matrix[0][c] = 0, 0
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
        if firstRowHasZero:
            for c in range(cols):
                matrix[0][c] = 0
        if firstColHasZero:
            for r in range(rows):
                matrix[r][0] = 0