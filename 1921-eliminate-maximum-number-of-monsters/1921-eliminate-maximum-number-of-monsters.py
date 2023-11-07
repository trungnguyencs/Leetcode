class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [d/s for d, s in zip(dist, speed)]
        time.sort()
        for i, t in enumerate(time):
            if i >= t:
                return i
        return len(time)