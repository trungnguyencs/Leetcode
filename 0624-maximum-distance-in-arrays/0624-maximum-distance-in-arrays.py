class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        Min = secondMin = float('inf')
        Max = secondMax = float('-inf')
        minIdx = maxIdx = 0
        for i, arr in enumerate(arrays):
            if arr[0] < Min:
                Min, secondMin, minIdx = arr[0], Min, i
            elif arr[0] < secondMin:
                secondMin = arr[0]
            if arr[-1] > Max:
                Max, secondMax, maxIdx = arr[-1], Max, i
            elif arr[-1] > secondMax:
                secondMax = arr[-1]
        return Max - Min if maxIdx != minIdx else max(Max - secondMin, secondMax - Min)