class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        #length of the side of biggest square will be 
        #1 + min(longest consecutive streak in hBars and vBars)
        hBars.sort()
        vBars.sort()
        maxH = self.maxConsecutive(hBars) + 1
        maxV = self.maxConsecutive(vBars) + 1
        return min(maxH, maxV) ** 2

    def maxConsecutive(self, arr):
        maxStreak = streak = 1
        prev = arr[0]
        for i in range(1, len(arr)):
            if arr[i] == prev + 1:
                streak += 1
                maxStreak = max(maxStreak, streak)
            else:
                streak = 1
            prev = arr[i]
        return maxStreak