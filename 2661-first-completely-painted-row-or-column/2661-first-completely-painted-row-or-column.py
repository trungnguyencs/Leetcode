class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        dic = {}
        rows = [0]*R
        cols = [0]*C
        for r in range(R):
            for c in range(C):
                dic[mat[r][c]] = (r, c)
        for i, num in enumerate(arr):
            r, c = dic[num]
            rows[r] += 1
            if rows[r] == C: return i
            cols[c] += 1
            if cols[c] == R: return i