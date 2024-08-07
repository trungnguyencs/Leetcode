class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        totalTime = duration
        for i in range(1, len(timeSeries)):
            totalTime += duration - max(0, timeSeries[i-1] + duration - timeSeries[i])
        return totalTime