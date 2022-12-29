# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        R, C = binaryMatrix.dimensions()
        r, c = 0, C - 1
        ans = -1
        while r < R and c >= 0:
            while c >= 0 and binaryMatrix.get(r, c) == 1:
                ans = c
                c -= 1
            r += 1
        return ans