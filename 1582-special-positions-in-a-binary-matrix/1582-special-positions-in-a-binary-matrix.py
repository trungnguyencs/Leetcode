class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cols, rows = Counter(), Counter()
        ans = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == rows[r] == cols[c] == 1:
                    ans += 1
        return ans