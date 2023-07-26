class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # since except the last train, each train takes at least 1 hour
        if hour <= len(dist) - 1: return -1
        l, r = 1, 10**7
        while l <= r:
            m = (l + r)//2
            if self.isOnTime(dist, hour, float(m)):
                r = m - 1
            else:
                l = m + 1
        return l
    
    def isOnTime(self, dist, hour, speed):
        time = 0
        for i, d in enumerate(dist):
            time += math.ceil(d/speed) if i != len(dist) - 1 else d/speed
        return time <= hour