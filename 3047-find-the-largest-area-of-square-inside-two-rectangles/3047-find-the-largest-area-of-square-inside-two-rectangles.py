class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        squares = list(zip(bottomLeft, topRight))
        squares.sort(key=lambda sq: [sq[0][0], sq[0][1]])
        maxOverlap = 0
        for i in range(len(squares) - 1):
            for j in range(i + 1, len(squares)):
                (ax1, ay1), (ax2, ay2) = squares[i]
                (bx1, by1), (bx2, by2) = squares[j]
                if bx1 > ax2: break
                overlap = self.getOverlap(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
                maxOverlap = max(maxOverlap, overlap)
        return maxOverlap

    def getOverlap(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        d1 = max(0, min(ax2, bx2) - max(ax1, bx1))
        d2 = max(0, min(ay2, by2) - max(ay1, by1))
        return min(d1, d2) ** 2