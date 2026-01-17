class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        squares = list(zip(bottomLeft, topRight))
        maxOverlap = 0
        for i in range(len(squares)):
            for j in range(len(squares)):
                if i != j:
                    overlap = self.getOverlap(squares[i], squares[j])
                    maxOverlap = max(maxOverlap, overlap)
        return maxOverlap

    def getOverlap(self, square1, square2):
        (ax1, ay1), (ax2, ay2) = square1
        (bx1, by1), (bx2, by2) = square2
        d1 = max(0, min(ax2, bx2) - max(ax1, bx1))
        d2 = max(0, min(ay2, by2) - max(ay1, by1))
        return min(d1, d2) ** 2