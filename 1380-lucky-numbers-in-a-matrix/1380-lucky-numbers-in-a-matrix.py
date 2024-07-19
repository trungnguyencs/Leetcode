class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        ans = []
        maxIndexes = set()
        for r, row in enumerate(matrix):
            maxIndexes.add((r, min(range(0, C), key=lambda c: row[c])))
        for r, c in maxIndexes:
            if matrix[r][c] == max([matrix[r1][c] for r1 in range(R)]):
                ans.append(matrix[r][c])
        return ans