# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, mat: 'BinaryMatrix') -> int:
        rowCount, colCount = mat.dimensions()
        c = colCount - 1
        minCol = -1
        for r in range(rowCount):
            while c >= 0 and mat.get(r, c) == 1:
                minCol = c
                c -= 1
        return minCol