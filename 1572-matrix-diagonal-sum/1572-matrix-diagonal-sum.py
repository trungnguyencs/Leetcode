class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        for i in range(n):
            s += mat[i][i] + mat[i][n - 1 - i]
        return s if n % 2 == 0 else s - mat[n//2][n//2]