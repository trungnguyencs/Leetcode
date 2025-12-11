class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        #for each row, store the min and max col indices
        #for each col, store the min and max row indices
        #then at any building we will know if it's covered in O(1)
        minX = defaultdict(lambda: float(inf))
        maxX = defaultdict(lambda: -float(inf))
        minY = defaultdict(lambda: float(inf))
        maxY = defaultdict(lambda: -float(inf))
        ans = 0
        for x, y in buildings:
            minX[y] = min(minX[y], x)
            maxX[y] = max(maxX[y], x)
            minY[x] = min(minY[x], y)
            maxY[x] = max(maxY[x], y)
        for x, y in buildings:
            ans += (minX[y] < x < maxX[y] and minY[x] < y < maxY[x])
        return ans