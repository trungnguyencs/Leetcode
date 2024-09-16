class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [self.toMinutes(s) for s in timePoints]
        minutes.sort()
        ans = minutes[0] + 24*60 - minutes[-1]
        for i in range(len(minutes) - 1):
            ans = min(ans, minutes[i+1] - minutes[i])
        return ans
        
    def toMinutes(self, s):
        h, m = s.split(':')
        return int(h) * 60 + int(m)