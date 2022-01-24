class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = self.bisectLeftRow(matrix, target)
        c = bisect_left(matrix[r], target)
        if c == len(matrix[0]): return False
        return matrix[r][c] == target
        
    def bisectLeftRow(self, matrix, target):
        l, r = 0, len(matrix)
        while l < r:
            m = (l + r)//2
            if matrix[m][0] > target:
                r = m
            else:
                l = m + 1
        # l is the left most position for target to be inserted
        # therefore target will be on line l if matrix[l][0] == target, on line l-1 otherwise
        return l if l < len(matrix) and matrix[l][0] == target else l-1
        