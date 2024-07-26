class Solution:
    def matrixReshape(self, mat: List[List[int]], R: int, C: int) -> List[List[int]]:
        if R * C != len(mat) * len(mat[0]): return mat
        ans = [[0]*C for _ in range(R)]
        r = c = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans[r][c] = mat[i][j]
                c += 1
                if c == C:
                    r, c = r + 1, 0
        return ans