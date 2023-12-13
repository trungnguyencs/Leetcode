class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        R, C = len(mat), len(mat[0])
        rows = [0]*R
        cols = [0]*C
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        for r in range(R):
            for c in range(C):
                if mat[r][c] == rows[r] == cols[c] == 1:
                    ans += 1
        return ans