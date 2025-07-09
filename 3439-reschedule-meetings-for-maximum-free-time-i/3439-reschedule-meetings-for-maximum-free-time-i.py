class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        #1. It's always optimal to combine k consecutive meetings
        #2. k meetings has k + 1 spaces, so answer is the largest window of size k + 1 in the distances array
        distances = self.getDistances(startTime, endTime, eventTime)
        window = 0
        for i in range(k + 1):
            window += distances[i]
        maxWindow = window
        for i in range(k + 1, len(distances)):
            window += distances[i] - distances[i - (k + 1)]
            maxWindow = max(maxWindow, window)
        return maxWindow

    def getDistances(self, startTime, endTime, eventTime):
        distances = []
        lastEnd = 0
        for s, e in zip(startTime, endTime):
            distances.append(s - lastEnd)
            lastEnd = e
        distances.append(eventTime - lastEnd)
        return distances