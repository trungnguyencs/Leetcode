class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m1, m2, M1, M2, minIdx, maxIdx = self.findMaxMin(arrays)
        return M1 - m1 if minIdx != maxIdx else max(M1 - m2, M2 - m1)
        
    def findMaxMin(self, arrays):
        min = secondMin = float('inf')
        max = secondMax = float('-inf')
        minIdx = maxIdx = 0
        for i, arr in enumerate(arrays):
            if arr[0] < min:
                min, secondMin, minIdx = arr[0], min, i
            elif arr[0] < secondMin:
                secondMin = arr[0]
            if arr[-1] > max:
                max, secondMax, maxIdx = arr[-1], max, i
            elif arr[-1] > secondMax:
                secondMax = arr[-1]
        return min, secondMin, max, secondMax, minIdx, maxIdx