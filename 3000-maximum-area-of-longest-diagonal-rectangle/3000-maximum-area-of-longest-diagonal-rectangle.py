class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiag = area = 0
        for w, h in dimensions:
            diag = w**2 + h**2
            if diag > maxDiag:
                maxDiag = diag
                area = w * h
            elif diag == maxDiag:
                area = max(area, w * h)
        return area